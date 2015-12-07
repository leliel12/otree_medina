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


class Section11Result(Page):

    timeout_seconds = Constants.result_time


class Section12(Page):

    form_model = models.Player
    form_fields = [
        'bolsa_o_25_con_seguridad',
        'bolsa_o_30_con_seguridad',
        'bolsa_o_35_con_seguridad',
        'bolsa_o_40_con_seguridad',
        'bolsa_o_45_con_seguridad',
        'bolsa_o_50_con_seguridad',
        'bolsa_o_55_con_seguridad',
        'bolsa_o_60_con_seguridad',
        'bolsa_o_65_con_seguridad',
        'bolsa_o_70_con_seguridad',
        'bolsa_o_75_con_seguridad',
        'bolsa_o_80_con_seguridad']

    def before_next_page(self):
        self.player.set_payoff_12()


page_sequence = [Welcome, Instructions, Section11, Section11Result, Section12]
