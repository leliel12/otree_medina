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
    pass


class Instructions(Page):

    timeout_seconds = Constants.instructions_time


class Section11(Page):

    timeout_seconds = Constants.section11_time

    form_model = models.Player
    form_fields = ["dispuesto_a_apostar"]

    def before_next_page(self):
        self.player.set_payoff_11()


page_sequence = [Welcome, Instructions, Section11]
