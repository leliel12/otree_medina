#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import itertools
import collections

import otree.constants_internal as constants

def float_as_percentage(a):
        return int(a * 100)


class TimeOutMixin(object):

    process_form_on_timeout = False

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        if request.POST.get(constants.auto_submit):
            self.timeout_happened = True  # for public API
        else:
            self.timeout_happened = False

        if self.timeout_happened == False or self.process_form_on_timeout:
            form = self.get_form(
                data=request.POST, files=request.FILES, instance=self.object)
            if form.is_valid():
                self.form = form
                self.object = form.save()
            else:
                return self.form_invalid(form)
        else:
            self._set_auto_submit_values()

        self.before_next_page()
        self._increment_index_in_pages()
        return self._redirect_to_page_the_user_should_be_on()


def round_robin(subssn):
    """Try to generate every group of players with a lesser probabilty to mix
    the same players twice.

    **Warning:** This is slow, really slow. Seriously, it is very slow.

    """

    def pxg2id(players):
        participant_ids = [player.participant_id for player in players]
        participant_ids.sort()
        pxg_id = "|".join(map(str, participant_ids))
        return pxg_id

    def usage_counts(subssn):
        counts = {}
        for p_subssn in subssn.in_previous_rounds():
            for players in players_x_groups(p_subssn):
                size = len(players)
                if size not in counts:
                    counts[size] = collections.defaultdict(int)
                pxg_id = pxg2id(players)
                counts[size][pxg_id] += 1
        return counts

    def combinations_by_sizes(groups, players, counts):
        sizes, combinations = [], {}
        for group in groups:
            size = len(group)
            sizes.append(size)
            if size not in combinations:
                combs = []
                for players in itertools.combinations(players, size):
                    pxg_id = pxg2id(players)
                    count = counts[size][pxg_id]
                    combs.append((count, players))
                combs.sort(key=lambda e: e[0])
                combinations[size] = [comb[1] for comb in combs]
        return tuple(sizes), combinations

    def shuffle_sizes(sizes):
        ssizes = list(sizes)
        random.shuffle(ssizes)
        return ssizes

    def create_groups(sizes, combinations):
        groups = []
        used_participants = set()
        for size in sizes:
            comb, end, candidate = combinations[size], False, None
            while comb and not end:
                candidate = comb.pop(0)
                participant_ids = [p.participant_id for p in candidate]
                if not used_participants.intersection(participant_ids):
                    used_participants.update(participant_ids)
                    end = True
            groups.append(candidate)
        return groups

    def sort_by_sizes(groups, sizes):
        by_sizes = collections.defaultdict(list)
        for group in groups:
            by_sizes[len(group)].append(group)
        sorted_groups = [by_sizes[size].pop() for size in sizes]
        return sorted_groups

    groups = players_x_groups(subssn)
    players = tuple(itertools.chain.from_iterable(groups))

    counts = usage_counts(subssn)
    sizes, combinations = combinations_by_sizes(groups, players, counts)
    ssizes = shuffle_sizes(sizes)
    shuffled_groups = create_groups(ssizes, combinations)
    groups = sort_by_sizes(shuffled_groups, sizes)
    return tuple(groups)
