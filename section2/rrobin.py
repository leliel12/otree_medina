#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from collections import defaultdict


def players_by_role(players):
        r1, r2 = [], []
        for p in players:
            if p.id_in_group_1() == 1:
                r1.append(p)
            else:
                r2.append(p)
        return r1, r2


def get_combs(r1, r2):
    combs = []
    for plyr_1 in r1:
        pr_id1 = plyr_1.participant.id
        for plyr_2 in r2:
            combs.append((pr_id1, plyr_2.participant.id))
    return combs


def count_combs(combs, subssn):
    cnts = {c: 0 for c in combs}
    for prev_subssn in subssn.in_previous_rounds():
        prev_groups = tuple(g.get_players() for g in prev_subssn.get_groups())
        for plyr_1, plyr_2 in prev_groups:
            key = (plyr_1.participant.id, plyr_2.participant.id)
            cnts[key] += 1

    reverse_d = defaultdict(list)
    for comb, cnt in cnts.items():
        reverse_d[cnt].append(comb)

    return dict(reverse_d)


def get_selected(cnt_combs, groups_n):
    by_size_suffle = []
    for cnt, combs in sorted(cnt_combs.items()):
        combs = list(combs)
        random.shuffle(combs)
        by_size_suffle.extend(combs)

    groups, used = set(), set()
    for p1, p2 in by_size_suffle:
        if p1 not in used and p2 not in used:
            groups.add((p1, p2))
            used.update((p1, p2))
        if len(groups) == groups_n:
            break
    return list(groups)


def round_robin_by_role(subssn):

    groups_n = len(subssn.get_groups()) # number of groups need to be created
    players = subssn.get_players() # all the players to be grouped
    p2p = {plyr.participant.id: plyr for plyr in players} # map participant to player

    pbr0, pbr1 = players_by_role(players) # split the players in the two roles

    combs = get_combs(pbr0, pbr1) # get all posible combinations of participants based in their roles
    cnt_combs = count_combs(combs, subssn) # how many times the combination was be used in previous rounc {cnt: [(p0, p1)...]}

    selected = get_selected(cnt_combs, groups_n)

    groups = [(p2p[p1], p2p[p2]) for p1, p2 in selected]

    return groups
