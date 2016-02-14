#!/usr/bin/env python
# -*- coding: utf-8 -*-


# =============================================================================
# IMPORTS
# =============================================================================

import csv
import argparse
import logging
import itertools

from django.core.management.base import BaseCommand

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
            '--out', dest="out", action='store', type=argparse.FileType('w'),
            help="output csv file")

    def next_user_info(self, users_info, idx):
        if users_info:
            return users_info.pop()
        logger.warning("To few users info: Default name for Participant '{}'".format(idx))
        return "Participant {}".format(idx), None

    def handle(self, sessioncode, conf, out, **options):
        session = Session.objects.get(code=sessioncode)
        users_info = list(csv.reader(conf))
        for idx, participant in enumerate(session.participant_set.all()):
            name, avatar = self.next_user_info(users_info, idx)
            players = (
                participant.section1_player.all(),
                participant.section2_player.all(),
                participant.questionnaire_player.all())
            for player in itertools.chain(*players):
                player.player_name = name
                player.avatar = avatar
                player.save()




