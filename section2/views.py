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


# =============================================================================
# NEGOCIACION SIMPLE
# =============================================================================

class NegociacionSimpleProponente(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 60

    form_model = models.Player
    form_fields = ["n_simple_propuesta"]

    def is_displayed(self):
       is_game = (self.subsession.get_current_game() == Constants.n_simple)
       is_role = (self.player.role() == Constants.proponente)
       return is_game and is_role


class NegociacionSimpleEsperarProponente(WaitPage):

    title_text = "Experando por la propuesta"
    body_text = "Usted es el Respondente y debe esperar al Proponente"


class NegociacionSimpleRespondente(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 60

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


class NegociacionSimpleRespuesta(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 60

    def vars_for_template(self):
        proponente = self.group.get_player_by_role(Constants.proponente)
        respondente = self.group.get_player_by_role(Constants.respondente)
        return {"respondente": respondente, "proponente": proponente}


# =============================================================================
# EMPRESA TRABAJADOR
# =============================================================================

class NegociacionEmpresaTrabajadorPropuesta(TimeOutMixin, Page):

    #~ process_form_on_timeout = True
    #~ timeout_seconds = 60

    form_model = models.Player
    form_fields = ["n_empresa_trabajador_propuesta"]

    def is_displayed(self):
        is_game = True or (self.subsession.get_current_game() == Constants.n_empresa_trabajador)
        is_role = (self.player.role() == Constants.empresa)
        return is_game and is_role

    def before_next_page(self):
        propuestas = self.player.n_empresa_trabajador_propuestas
        propuestas.append(int(self.player.n_empresa_trabajador_propuesta))
        self.player.n_empresa_trabajador_propuestas = propuestas


class  NegociacionEmpresaTrabajadorEsperarEmpresa(WaitPage):

    title_text = "Experando por la propuesta"
    body_text = "Usted es el Trabajador y debe esperar a la Empresa"


class NegociacionEmpresaTrabajadorRespuesta(TimeOutMixin, Page):

    #~ process_form_on_timeout = True
    #~ timeout_seconds = 60

    form_model = models.Player
    form_fields = ["n_empresa_trabajador_respuesta", "n_empresa_trabajador_contrapropuesta"]

    def vars_for_template(self):
        empresa = self.group.get_player_by_role(Constants.empresa)
        return {
            "propuesta": empresa.n_empresa_trabajador_propuesta,
            "ganancia": 200 - empresa.n_empresa_trabajador_propuesta
        }

    def n_empresa_trabajador_contrapropuesta_choices(self):
        empresa = self.group.get_player_by_role(Constants.empresa)
        lower = empresa.n_empresa_trabajador_propuesta + 1
        if lower > 200:
            lower = 200
        return list(range(lower, 201))

    def is_displayed(self):
        is_game = True or (self.subsession.get_current_game() == Constants.n_empresa_trabajador)
        is_role = (self.player.role() == Constants.trabajador)
        return is_game and is_role

    def before_next_page(self):
        contrapropuestas = self.player.n_empresa_trabajador_contrapropuestas
        contrapropuestas.append(int(self.player.n_empresa_trabajador_contrapropuesta))
        if self.player.n_empresa_trabajador_respuesta == "Rechazar":
            self.group.forzar_finalizacion_empresa_trabajador()

class  NegociacionEmpresaTrabajadorEsperarTrabajador(WaitPage):

    title_text = "Experando por la respuesta"
    body_text = "Usted es la Empresa y debe esperar al Trabajador"






page_sequence = [
    #~ Instructions,

    #~ NegociacionSimpleProponente, NegociacionSimpleEsperarProponente,
    #~ NegociacionSimpleRespondente, NegociacionSimpleEsperarRespondente,
    #~ NegociacionSimpleRespuesta

    NegociacionEmpresaTrabajadorPropuesta, NegociacionEmpresaTrabajadorEsperarEmpresa,
    NegociacionEmpresaTrabajadorRespuesta, NegociacionEmpresaTrabajadorEsperarTrabajador



]
