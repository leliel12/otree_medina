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

VERSION = "0.3"

# =============================================================================
# COMMND
# =============================================================================

class Command(BaseCommand):
    help = ("Show version of otree medina")

    def handle(self, **options):
        print("oTree Medina Version: " + VERSION)
