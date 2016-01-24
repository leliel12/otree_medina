# -*- coding: utf-8 -*-
from __future__ import division
from django.utils import timezone

from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

from utils import TimeOutMixin


def vars_for_all_templates(self):

    return {}


class Welcome(Page):
    pass


class Instructions(Page):

    timeout_seconds = 20


class Section11(TimeOutMixin, Page):

    process_form_on_timeout = True

    timeout_seconds = 90

    form_model = models.Player
    form_fields = ["dispuesto_a_apostar"]

    def before_next_page(self):
        self.player.set_payoff_11()


class Section11Result(Page):

    timeout_seconds = 20

    def _set_auto_submit_values(self):
        pass


class Section12(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 120

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

    def _set_auto_submit_values(self): pass

    def before_next_page(self):
        self.player.set_payoff_12()

class Section12Result(Page):

    timeout_seconds = 30

    def vars_for_template(self):
        parts = self.player.caso_seleccionado_para_12.split("_")
        parts.insert(3, "ECUS")

        eligio_seguridad = getattr(
            self.player, self.player.caso_seleccionado_para_12) == "seguridad"

        return {"caso_as_text": " ".join(parts).title(),
                "eligio_seguridad": eligio_seguridad,
                "seguridad_gano": parts[2]}


page_sequence = [
    Welcome, Instructions, Section11, Section11Result,
    Section12, Section12Result]
