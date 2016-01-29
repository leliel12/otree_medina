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


class Instructions(Page):

    timeout_seconds = 60 * 5

    def is_displayed(self):
        return self.subsession.round_number == 1


class NegociacionSimpleProponente(Page):

    form_model = models.Player
    form_fields = ["n_simple_propuesta"]

    def is_displayed(self):
       is_game = (self.subsession.get_current_game() == Constants.n_simple)
       is_role = (self.player.role() == Constants.proponente)
       return is_game and is_role


class NegociacionSimpleEsperarProponente(WaitPage):

    title_text = "Experando por la propuesta"
    body_text = "Usted es el Respondente y debe esperar al Proponente"


class NegociacionSimpleRespondente(Page):

    form_model =  models.Player
    form_fields = ["n_simple_respuesta"]

    def vars_for_template(self):
        proponente = self.group.get_player_by_role(Constants.proponente)
        return {"proponente": proponente}

    def is_displayed(self):
        is_game = (self.subsession.get_current_game() == Constants.n_simple)
        is_role = (self.player.role() == Constants.respondente)
        return is_game and is_role


class NegociacionSimpleEsperarRespondente(WaitPage):

    title_text = "Experando por la respuesta"
    body_text = "Esperando a que el Respondente acepte o rechace su propuesta"

    def after_all_players_arrive(self):
        self.group.set_negociacion_simple_payoff()


class NegociacionSimpleRespuesta(Page):

    def vars_for_template(self):
        proponente = self.group.get_player_by_role(Constants.proponente)
        respondente = self.group.get_player_by_role(Constants.respondente)
        return {"respondente": respondente, "proponente": proponente}


page_sequence = [
    #Instructions,

    NegociacionSimpleProponente, NegociacionSimpleEsperarProponente,
    NegociacionSimpleRespondente, NegociacionSimpleEsperarRespondente,
    NegociacionSimpleRespuesta]
