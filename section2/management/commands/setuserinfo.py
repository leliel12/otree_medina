#!/usr/bin/env python
# -*- coding: utf-8 -*-


# =============================================================================
# IMPORTS
# =============================================================================
from __future__ import print_function

import csv
import argparse
import logging
import itertools

from django.core.management.base import BaseCommand, CommandError

from otree.models import Session
from section2 import models


# =============================================================================
# LOGGER
# =============================================================================

logger = logging.getLogger('otree')



# =============================================================================
# COMMND
# =============================================================================

class Command(BaseCommand):
    help = ("Set avatar and names to the session")

    def add_arguments(self, parser):
        ahelp = "session to store the avatars"
        parser.add_argument(
            '--session', dest="sessioncode", action='store', help=ahelp),
        parser.add_argument(
            '--conf', dest="conf", action='store', type=argparse.FileType('r'),
            help="configuration CSV file"),
        parser.add_argument(
            '--host', dest="host", action='store', default="localhost:8000",
            help="host where the project is running"),
        parser.add_argument(
            '--out', dest="out", action='store', type=argparse.FileType('w'),
            help="output csv file")

    def next_user_info(self, users_info, idx):
        info = users_info.pop()
        return info["Name"], info["Avatar"], info["Gender"], info["Email"]

    def link(self, participant, host):
        return "http://{}{}".format(host, participant._start_url())

    def handle(self, sessioncode, conf, host, out, **options):
        session = Session.objects.get(code=sessioncode)
        participants = session.participant_set
        users_info = list(csv.DictReader(conf))

        if participants.count() != len(users_info):
            msg = "The session '{}' has {} participants. and the configuration file '{}' is for {} participants"
            raise CommandError(msg.format(sessioncode, participants.count(), conf.name, len(users_info)))

        writer = csv.writer(out)
        for idx, participant in enumerate(participants.all()):
            url = self.link(participant, host)
            name, avatar, gender, email = self.next_user_info(users_info, idx)
            players = (
                participant.section1_player.all(),
                participant.section2_player.all(),
                participant.questionnaire_player.all())
            for player in itertools.chain(*players):
                player.player_name = name
                player.avatar = avatar
                player.genero = gender
                player.save()
            print(name, avatar, gender, email, url)
            writer.writerow([name, avatar, gender, email, url])
