# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
import json
from otree.db import models
import otree.models
from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>


doc = """
Foo
"""


source_code = ""


bibliography = ()


links = {}


keywords = ()

class Constants:
    name_in_url = 'section2'
    players_per_group = 2
    num_rounds = 16

    n_simple = u"Negociación Simple"
    n_simple_rounds = [1, 8]
    proponente, respondente = "Proponente", "Respondente"

    n_empresa_trabajador = u"Negociación Empresa Trabajador"
    n_empresa_trabajador_rounds = [9, 16]
    empresa, trabajador = "Empresa", "Trabajador"

    initial_payoff = c(100)


class Subsession(otree.models.BaseSubsession):

    def before_session_starts(self):
        self.match_players("round_robin")

    def get_current_game(self):
        if self.round_number <= Constants.n_simple_rounds[-1]:
            return Constants.n_simple
        return Constants.n_empresa_trabajador


class Group(otree.models.BaseGroup):

    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    n_empresa_trabajador_finalizacion_forzada = models.BooleanField(default=False)
    n_empresa_trabajador_fin_ciclo = models.BooleanField(default=False)

    def set_negociacion_simple_payoff(self):
        proponente = self.get_player_by_role(Constants.proponente)
        respondente = self.get_player_by_role(Constants.respondente)
        if respondente.n_simple_respuesta == "Aceptar":
            proponente.payoff = 200 - proponente.n_simple_propuesta
            respondente.payoff = proponente.n_simple_propuesta
        else:
            proponente.payoff = 0
            respondente.payoff = 0

    def forzar_finalizacion_empresa_trabajador(self):
        finalizar = random.randint(1, 100) <= 20
        if False and finalizar:
            self.n_empresa_trabajador_finalizacion_forzada = False


class Player(otree.models.BasePlayer):

    # <built-in>
    group = models.ForeignKey(Group, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    n_simple_propuesta = models.CurrencyField(
        choices=range(0, 201), verbose_name="¿Cuánto le gustaría ofrecer?", default=0)
    n_simple_respuesta = models.CharField(
        widget=widgets.RadioSelectHorizontal(),
        max_length=250, choices=["Aceptar", "Rechazar"], default="Aceptar")

    n_empresa_trabajador_propuesta = models.CurrencyField(
        verbose_name="¿Cuánto le gustaría ofrecer como salario?", choices=range(0, 201), default=0)
    n_empresa_trabajador_propuestas = models.TextField(default="[]")

    n_empresa_trabajador_respuesta = models.CharField(
        widget=widgets.RadioSelectHorizontal(),
        max_length=250, choices=["Aceptar", "Rechazar"], default="Aceptar")
    n_empresa_trabajador_contrapropuesta = models.CurrencyField(
        verbose_name="Contraoferta de salario:", choices=range(0, 201), default=0)
    n_empresa_trabajador_contrapropuestas = models.TextField(default="[]")

    n_empresa_trabajador_finalizacion_forzada = models.BooleanField(default=False)

    def add_propuesta(self, v):
        lista = json.loads(self.n_empresa_trabajador_propuestas)
        lista.append(int(v))
        self.n_empresa_trabajador_propuestas = json.dumps(lista)

    def add_contrapropuesta(self, v):
        lista = json.loads(self.n_empresa_trabajador_contrapropuestas)
        lista.append(int(v))
        self.n_empresa_trabajador_contrapropuestas = json.dumps(lista)


    def role(self):
        #~ if self.subsession.get_current_game() == Constants.n_simple:
            #~ if self.id_in_group == 1:
                #~ return Constants.proponente
            #~ elif self.id_in_group == 2:
                #~ return Constants.respondente
        #~ elif self.subsession.get_current_game() == Constants.n_empresa_trabajador:
            if self.id_in_group == 1:
                return Constants.empresa
            elif self.id_in_group == 2:
                return Constants.trabajador
