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

import os
from django.conf import settings
from collections import defaultdict, Counter


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

    default_avatar = os.path.join(settings.BASE_DIR, "_static", "global", "default_avatar.png")
    default_avatar_b64 = "data:image/{};base64,{}".format(
        default_avatar.rsplit(".", 1)[1].lower(),
        open(default_avatar).read().encode("base64")
    )


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
        if self.round_number > 1:
            counts = self.usage_counts()
            players = self.get_players()
            by_role = self.players_by_role(players)

            used, selected = set(), []
            for p1 in by_role[1]:
                for p2 in by_role[2]:
                    key = self.to_key(p1, p2)
                    if key not in counts and key[0] not in used and key[1] not in used:
                        selected.append((p1, p2))
                        used.update(key)

            if len(used) < len(players):
                count_list = [e[0] for e in reversed(counts.most_common())]
                while len(used) < len(players):
                    key = count_list.pop(0)
                    if key[0] not in used and key[1] not in used:
                        p1, p2 = self.to_players(key, by_role)
                        selected.append((p1, p2))
                        used.update(key)
            self.set_groups(selected)

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

    def forzar_finalizacion_empresa_trabajador(self):
        finalizar = random.randint(1, 100) <= 20
        if False and finalizar:
            self.n_empresa_trabajador_finalizacion_forzada = True
            self.n_empresa_trabajador_fin_ciclo = True


class Player(otree.models.BasePlayer):

    # <built-in>
    group = models.ForeignKey(Group, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    player_name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)

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
