# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
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
    name_in_url = 'section1'
    players_per_group = None
    num_rounds = 1
    initial_payoff = c(100)
    instructions_time = 10
    section11_time = 3 * 60 # 3 minutes


class Subsession(otree.models.BaseSubsession):

    def before_session_starts(self):
        for player in self.get_players():
            player.payoff = Constants.initial_payoff


class Group(otree.models.BaseGroup):

    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>


class Player(otree.models.BasePlayer):

    # <built-in>
    group = models.ForeignKey(Group, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    dispuesto_a_apostar = models.CurrencyField(
        default=0,
        choices=map(c, [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
    gano_apuesta = models.BooleanField()


    def set_payoff_11(self):
        self.gano_apuesta = random.choice([True, False])
        if self.dispuesto_a_apostar == 0:
            self.payoff += 100
        elif self.gano_apuesta:
            self.payoff += self.dispuesto_a_apostar * 3
        else:
            self.payoff -= self.dispuesto_a_apostar




