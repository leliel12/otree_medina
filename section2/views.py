# -*- coding: utf-8 -*-
from __future__ import division
from django.utils import timezone

from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

from utils import TimeOutMixin


def vars_for_all_templates(self):
    if self.subsession.show_avatar():
        return {"oponente": self.player.get_others_in_group()[0]}
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
        if self.subsession.get_current_game() == Constants.n_simple:
            self.group.set_negociacion_simple_payoff()


class NegociacionSimpleRespuesta(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 60

    def is_displayed(self):
        return self.subsession.get_current_game() == Constants.n_simple

    def vars_for_template(self):
        proponente = self.group.get_player_by_role(Constants.proponente)
        respondente = self.group.get_player_by_role(Constants.respondente)
        return {"respondente": respondente, "proponente": proponente}


# =============================================================================
# EMPRESA TRABAJADOR
# =============================================================================

class NegociacionEmpresaTrabajadorPropuesta(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 60

    form_model = models.Player
    form_fields = ["n_empresa_trabajador_propuesta"]

    def is_displayed(self):
        is_game = (self.subsession.get_current_game() == Constants.n_empresa_trabajador)
        is_role = (self.player.role() == Constants.empresa)
        return is_game and is_role

    def before_next_page(self):
        self.player.add_propuesta(self.player.n_empresa_trabajador_propuesta)


class  NegociacionEmpresaTrabajadorEsperarEmpresa(WaitPage):

    title_text = "Experando por la propuesta"
    body_text = "Usted es el Trabajador y debe esperar a la Empresa"


class NegociacionEmpresaTrabajadorRespuesta(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 60

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
        is_game = (self.subsession.get_current_game() == Constants.n_empresa_trabajador)
        is_role = (self.player.role() == Constants.trabajador)
        return is_game and is_role

    def before_next_page(self):
        if self.player.n_empresa_trabajador_respuesta == "Rechazar":
            self.player.add_contrapropuesta(self.player.n_empresa_trabajador_contrapropuesta)
        else:
            self.group.n_empresa_trabajador_fin_ciclo = True


class NegociacionEmpresaTrabajadorEsperarTrabajador(WaitPage):

    title_text = "Experando por la respuesta"
    body_text = "Usted es la Empresa y debe esperar al Trabajador"


# ===============
# CICLE
# ===============

class NegociacionEmpresaTrabajadorContraPropuesta(TimeOutMixin, Page):

    form_model = models.Player
    form_fields = ["n_empresa_trabajador_respuesta", "n_empresa_trabajador_propuesta"]
    template_name = "section2/NegociacionEmpresaTrabajadorContraPropuesta.html"

    def vars_for_template(self):
        trabajador = self.group.get_player_by_role(Constants.trabajador)
        return {
            "contrapropuesta": trabajador.n_empresa_trabajador_contrapropuesta}

    def n_empresa_trabajador_propuesta_choices(self):
        lower = self.player.n_empresa_trabajador_propuesta
        trabajador = self.group.get_player_by_role(Constants.trabajador)
        upper = trabajador.n_empresa_trabajador_contrapropuesta
        if upper <= 1:
            upper = 2
        return list(range(lower, upper))

    def is_displayed(self):
        is_game = (self.subsession.get_current_game() == Constants.n_empresa_trabajador)
        is_role = (self.player.role() == Constants.empresa)
        in_cicle = not self.group.n_empresa_trabajador_fin_ciclo
        return is_game and is_role and in_cicle

    def before_next_page(self):
        if self.player.n_empresa_trabajador_respuesta == "Rechazar":
            self.player.add_propuesta(self.player.n_empresa_trabajador_propuesta)
            self.group.forzar_finalizacion_empresa_trabajador()
        else:
            self.group.n_empresa_trabajador_fin_ciclo = True


class NegociacionEmpresaTrabajadorEsperarNuevaPropuestaEmpresa(WaitPage):

    title_text = "Experando por la propuesta"
    body_text = "Usted es el Trabajador y debe esperar a la Empresa"


class NegociacionEmpresaTrabajadorRespuestaContraPropuesta(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 60

    form_model = models.Player
    form_fields = ["n_empresa_trabajador_respuesta", "n_empresa_trabajador_contrapropuesta"]
    template_name = "section2/NegociacionEmpresaTrabajadorRespuestaContraPropuesta.html"

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
        is_game = (self.subsession.get_current_game() == Constants.n_empresa_trabajador)
        is_role = (self.player.role() == Constants.trabajador)
        in_cicle = not self.group.n_empresa_trabajador_fin_ciclo
        return is_game and is_role and in_cicle

    def before_next_page(self):
        if self.player.n_empresa_trabajador_respuesta == "Rechazar":
            self.player.add_contrapropuesta(self.player.n_empresa_trabajador_contrapropuesta)
            self.group.forzar_finalizacion_empresa_trabajador()
        else:
            self.group.n_empresa_trabajador_fin_ciclo = True


class NegociacionEmpresaTrabajadorEsperarTrabajadorDeNuevo(WaitPage):

    title_text = "Experando por la respuesta"
    body_text = "Usted es la Empresa y debe esperar al Trabajador"


to_cicle = [
    NegociacionEmpresaTrabajadorContraPropuesta, # EMPRESA PROPONE DENUEVO
    NegociacionEmpresaTrabajadorEsperarNuevaPropuestaEmpresa, # TRABAJADOR ESPERA
    NegociacionEmpresaTrabajadorRespuestaContraPropuesta, # TRABAJADOR CONTRA PROPONE DENUEVO
    NegociacionEmpresaTrabajadorEsperarTrabajadorDeNuevo, # EMPRESA ESPERA
]
cicle = []
for idx in range(1):
    cicle.extend(
        type("{}{}".format(cls.__name__, idx), (cls,), {}) for cls in to_cicle)

globals().update({cls.__name__:cls for cls in cicle})


# =============================================================================
# FINAL
# =============================================================================

class NegociacionEmpresaResolveResult(WaitPage):
    title_text = "Calculando resultado"
    body_text = "Calculando resultado"

    def after_all_players_arrive(self):
        if self.subsession.get_current_game() == Constants.n_empresa_trabajador:
            if self.group.n_empresa_trabajador_fin_ciclo == False:
                self.group.n_empresa_trabajador_finalizacion_forzada =True
                self.group.n_empresa_trabajador_fin_ciclo = True
            self.group.set_negociacion_empresa_trabajador_payoff()


class NegociacionEmpresaTrabajadorResult(TimeOutMixin, Page):

    def is_displayed(self):
        return self.subsession.get_current_game() == Constants.n_empresa_trabajador

    def vars_for_template(self):
        fin_forzado = self.group.n_empresa_trabajador_finalizacion_forzada

        empresa = self.group.get_player_by_role(Constants.empresa)
        propuestas = empresa.all_propuestas()

        trabajador = self.group.get_player_by_role(Constants.trabajador)
        contrapropuestas = trabajador.all_contrapropuestas()
        lineas = []
        for idx, propuesta in enumerate(propuestas):
            linea = {
                "propuesta": c(propuesta),
                "contrapropuesta": c(contrapropuestas[idx]) if len(contrapropuestas) > idx else None}
            lineas.append(linea)
        acepto_empresa = not fin_forzado and len(propuestas) == len(contrapropuestas)
        acepto_trabajador = not fin_forzado and not acepto_empresa
        return {
            "fin_forzado": fin_forzado,
            "empresa": empresa,
            "trabajador": trabajador,
            "lineas": lineas,
            "acepto_empresa": acepto_empresa,
            "acepto_trabajador": acepto_trabajador}


page_sequence = [
    Instructions,

    NegociacionSimpleProponente, NegociacionSimpleEsperarProponente,
    NegociacionSimpleRespondente, NegociacionSimpleEsperarRespondente,
    NegociacionSimpleRespuesta,

    NegociacionEmpresaTrabajadorPropuesta, NegociacionEmpresaTrabajadorEsperarEmpresa,
    NegociacionEmpresaTrabajadorRespuesta, NegociacionEmpresaTrabajadorEsperarTrabajador
] + cicle + [NegociacionEmpresaResolveResult, NegociacionEmpresaTrabajadorResult]
