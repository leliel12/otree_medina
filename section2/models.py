# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
import json
from otree.db import models
import otree.models
from otree import widgets
from otree.common import Currency as c, currency_range
import random
import itertools
# </standard imports>

import os
from django.conf import settings
from collections import defaultdict, Counter

from utils import round_robin


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
    n_simple_rounds = [1, 3, 5, 7, 9, 11, 13]
    proponente, respondente = "Proponente", "Respondente"

    n_simple_virtual = u"Negociación Simple Virtual"
    n_simple_virtual_rounds = [15]

    n_empresa_trabajador = u"Negociación Empresa Trabajador"
    n_empresa_trabajador_rounds = [2, 4, 6, 8, 10, 12, 14]
    empresa, trabajador = "Empresa", "Trabajador"

    n_empresa_trabajador_virtual = u"Negociación Empresa Trabajador Virtual"
    n_empresa_trabajador_virtual_rounds = [16]

    hombre_blanco, hombre_oscuro = "hombre_blanco.jpg", "hombre_oscuro.jpg"
    mujer_blanca, mujer_oscura = "mujer_blanca.jpg", "mujer_oscura.jpg"

    virtual_comb = {
        "hombre_blanco_mujer_oscura": [hombre_blanco, mujer_oscura],
        "hombre_oscuro_mujer_blanca": [hombre_oscuro, mujer_blanca],
        "mujer_blanca_hombre_oscuro": [mujer_blanca, hombre_oscuro],
        "mujer_oscura_hombre_blanco": [mujer_oscura, hombre_blanco],
    }

    initial_payoff = c(100)

    default_avatar = os.path.join(settings.BASE_DIR, "_static", "global", "default_avatar.png")
    default_avatar_b64 = "data:image/{};base64,{}".format(
        default_avatar.rsplit(".", 1)[1].lower(),
        open(default_avatar).read().encode("base64")
    )

    finalizar_muestra = ([True] * 20 + [False] * 80)


class Subsession(otree.models.BaseSubsession):

    def players_by_role(self, players):
        by_role = defaultdict(list)
        for p in players:
            by_role[p.id_in_group].append(p)
        return dict(by_role)

    def to_key(self, p1, p2):
        return p1.participant_id, p2.participant_id

    def usage_counts(self):
        combs = []
        for p_subssn in self.in_previous_rounds():
            for g in self.get_groups():
                p1, p2 = g.get_players()
                combs.append(self.to_key(p1, p2))
        return Counter(combs)

    def to_players(self, key, by_role):
        p1, p2 = None, None
        for p in by_role[1]:
            if p.participant_id == key[0]:
                p1 = p
                break
        for p in by_role[2]:
            if p.participant_id == key[1]:
                p2 = p
                break
        return p1, p2

    def before_session_starts(self):
        players = self.get_players()
        if self.round_number == 1:
            virtual_comb = list(Constants.virtual_comb.keys())
            random.shuffle(virtual_comb)
            repeat = itertools.cycle(virtual_comb)
            for p in players:
                p.virtual_oponent = next(repeat)
        else:
            selected = round_robin(self)
            self.set_groups(selected)

            for ply in players:
                ply.virtual_oponent = ply.in_round(1).virtual_oponent

    def get_current_game(self):
        if self.round_number in Constants.n_simple_rounds:
            return Constants.n_simple
        elif self.round_number in Constants.n_simple_virtual_rounds:
            return Constants.n_simple_virtual
        elif self.round_number in Constants.n_empresa_trabajador_rounds:
            return Constants.n_empresa_trabajador
        return Constants.n_empresa_trabajador_virtual

    def show_avatar(self):
        return self.round_number > 8

    def tipo_oponente(self, player):
        current_game = self.get_current_game()
        role = player.role()
        if current_game == Constants.n_simple:
            return Constants.respondente if role == Constants.proponente else Constants.proponente
        elif current_game == Constants.n_empresa_trabajador:
            return Constants.trabajador if role == Constants.empresa else Constants.empresa

    def get_result_timeout(self):
        if self.round_number <= 3:
            return 30
        elif self.round_number <= 6:
            return 20
        return 15


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

    def set_negociacion_simple_virtual_payoff(self, proponente):
        proponente.payoff = 200 - proponente.n_simple_propuesta

    def set_negociacion_empresa_trabajador_payoff(self):
        empresa = self.get_player_by_role(Constants.empresa)
        trabajador = self.get_player_by_role(Constants.trabajador)
        if self.n_empresa_trabajador_finalizacion_forzada:
            empresa.payoff = c(50)
            trabajador.payoff = 0
        else:
            propuestas = empresa.all_propuestas()
            contrapropuestas = trabajador.all_contrapropuestas()
            X = c(
                contrapropuestas[-1]
                if len(propuestas) == len(contrapropuestas) else
                propuestas[-1])
            trabajador.payoff = X
            empresa.payoff = 200 - X

    def set_negociacion_empresa_trabajador_virtual_payoff(self, empresa):
        empresa.payoff = 200 - empresa.n_empresa_trabajador_propuesta

    def forzar_finalizacion_empresa_trabajador(self):
        finalizar = random.choice(Constants.finalizar_muestra)
        if finalizar:
            self.n_empresa_trabajador_finalizacion_forzada = True
            self.n_empresa_trabajador_fin_ciclo = True


class Player(otree.models.BasePlayer):

    # <built-in>
    group = models.ForeignKey(Group, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    player_name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)

    virtual_oponent = models.CharField(max_length=255, choices=list(Constants.virtual_comb.keys()))

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

    def all_propuestas(self):
        return json.loads(self.n_empresa_trabajador_propuestas)

    def add_propuesta(self, v):
        lista = self.all_propuestas()
        lista.append(int(v))
        self.n_empresa_trabajador_propuestas = json.dumps(lista)

    def all_contrapropuestas(self):
        return json.loads(self.n_empresa_trabajador_contrapropuestas)

    def add_contrapropuesta(self, v):
        lista = self.all_contrapropuestas()
        lista.append(int(v))
        self.n_empresa_trabajador_contrapropuestas = json.dumps(lista)

    def role(self):
        if self.subsession.get_current_game() == Constants.n_simple:
            if self.id_in_group == 1:
                return Constants.proponente
            elif self.id_in_group == 2:
                return Constants.respondente
        elif self.subsession.get_current_game() == Constants.n_empresa_trabajador:
            if self.id_in_group == 1:
                return Constants.empresa
            elif self.id_in_group == 2:
                return Constants.trabajador

    def avatarb64(self):
        if not self.avatar:
            return Constants.default_avatar_b64
        if not hasattr(self, "_avatarb64"):
            path = os.path.join(settings.BASE_DIR, "participants_conf", self.avatar)
            with open(path) as fp:
                self._avatarb64 = "data:image/{};base64,{}".format(
                    self.avatar.rsplit(".", 1)[1].lower(),
                    fp.read().encode("base64")
                )
        return self._avatarb64
