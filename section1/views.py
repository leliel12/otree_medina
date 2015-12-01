# -*- coding: utf-8 -*-
from __future__ import division
from django.utils import timezone

from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

def vars_for_all_templates(self):

    return {}


class Welcome(Page):

    def before_next_page(self):
        self.player.instructions_start_time = timezone.now()


class Instructions(Page):

    timeout_seconds = Constants.instructions_time


page_sequence = [Welcome, Instructions]
