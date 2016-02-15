#!/usr/bin/env python
# -*- coding: utf-8 -*-


# =============================================================================
# IMPORTS
# =============================================================================
from __future__ import print_function, unicode_literals

import csv
import argparse
import logging
import itertools

from django.core.management.base import BaseCommand

from otree.models import Session


# =============================================================================
# LOGGER
# =============================================================================

logger = logging.getLogger('otree')



# =============================================================================
# COMMND
# =============================================================================

class Command(BaseCommand):
    help = ("List al available sessions")

    def handle(self, **options):
        for session in Session.objects.all():
            stype = session.session_type
            participants = session.participant_set.count()
            msg = "- {}: {} - Participants: {} - Sequence: {}".format(
                stype["display_name"], session.code, participants,
                ", ".join(stype["app_sequence"]))
            print(msg)
        print("")
