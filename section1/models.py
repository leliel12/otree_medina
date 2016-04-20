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

    player_name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)

    # section 1.1
    dispuesto_a_apostar = models.CurrencyField(
        default=0,
        choices=map(c, [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
    gano_apuesta = models.BooleanField()

    # section 1.2
    bolsa_o_25_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "25 ECUs con seguridad")])
    #~ gano_bolsa_o_25_con_seguridad = models.PositiveIntegerField()

    bolsa_o_30_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "30 ECUs con seguridad")])
    #~ gano_bolsa_o_30_con_seguridad = models.PositiveIntegerField()

    bolsa_o_35_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "35 ECUs con seguridad")])
    #~ gano_bolsa_o_35_con_seguridad = models.PositiveIntegerField()

    bolsa_o_40_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "40 ECUs con seguridad")])
    #~ gano_bolsa_o_40_con_seguridad = models.PositiveIntegerField()

    bolsa_o_45_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "45 ECUs con seguridad")])
    #~ gano_bolsa_o_45_con_seguridad = models.PositiveIntegerField()

    bolsa_o_50_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "50 ECUs con seguridad")])
    #~ gano_bolsa_o_50_con_seguridad = models.PositiveIntegerField()

    bolsa_o_55_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "55 ECUs con seguridad")])
    #~ gano_bolsa_o_55_con_seguridad = models.PositiveIntegerField()

    bolsa_o_60_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "60 ECUs con seguridad")])
    #~ gano_bolsa_o_60_con_seguridad = models.PositiveIntegerField()

    bolsa_o_65_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "65 ECUs con seguridad")])
    #~ gano_bolsa_o_65_con_seguridad = models.PositiveIntegerField()

    bolsa_o_70_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "70 ECUs con seguridad")])
    #~ gano_bolsa_o_70_con_seguridad = models.PositiveIntegerField()

    bolsa_o_75_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "75 ECUs con seguridad")])
    #~ gano_bolsa_o_75_con_seguridad = models.PositiveIntegerField()

    bolsa_o_80_con_seguridad = models.CharField(
        max_length=255, widget=widgets.RadioSelectHorizontal(), default="bolsa",
        choices=[("bolsa", "Seleccionar de la bolsa"), ("seguridad", "80 ECUs con seguridad")])
    #~ gano_bolsa_o_80_con_seguridad = models.PositiveIntegerField()

    caso_seleccionado_para_12 = models.CharField(max_length=255)
    color_bola_al_azar = models.CharField(max_length=50, choices=["blanca", "roja"])

    def set_payoff_11(self):
        self.gano_apuesta = random.choice([True, False])
        if self.gano_apuesta:
            self.payoff += (self.dispuesto_a_apostar * 3) - self.dispuesto_a_apostar
        else:
            self.payoff -= self.dispuesto_a_apostar

    def set_payoff_12(self):
        caso_ecus = random.choice([25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
        self.caso_seleccionado_para_12 = "bolsa_o_{}_con_seguridad".format(caso_ecus)
        seleccion = getattr(self, self.caso_seleccionado_para_12)
        if seleccion == "seguridad":
            self.payoff += caso_ecus
        else:
            self.color_bola_al_azar = random.choice(["roja", "blanca"])
            if self.color_bola_al_azar == "blanca":
                self.payoff += 100
