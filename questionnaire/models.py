# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division, unicode_literals
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
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1



class Subsession(otree.models.BaseSubsession):
    pass


class Group(otree.models.BaseGroup):

    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>


class Player(otree.models.BasePlayer):

    # <built-in>
    group = models.ForeignKey(Group, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    # bloque 1
    satisfecho_con_la_vida = models.PositiveIntegerField(
        verbose_name=(
            "En una escala del 1 al 10, donde 1 es nada satisfecho y 10 "
            "totalmente satisfecho, en general ¿qué tan satisfecha(o) se "
            "encuentra usted con su vida? Usted puede escoger cualquier "
            "número entre 1 y 10."), choices=range(1,11),
            widget=widgets.RadioSelectHorizontal(), default=1)

    cuartos_en_el_hogar = models.PositiveIntegerField(
        verbose_name=("¿Cuántos cuartos hay en su hogar sin contar pasillos, ni baños?"), min=1, default=1)

    cuantos_cuartos_se_usan_para_dormir = models.PositiveIntegerField(
        verbose_name=("Y de esos cuartos, ¿cuántos usan para dormir?"), min=1, default=1)

    habitantes = models.PositiveIntegerField(
        verbose_name=("¿Cuántas personas viven en su hogar contando ancianos y niños?"), min=1, default=1)

    focos = models.PositiveIntegerField(
        verbose_name=(
            "Contando todos los focos que utiliza para iluminar su hogar, "
            "incluyendo los de techos, paredes y lámparas de buró o piso, "
            "dígam, ¿Cuántos focos tiene en su vivienda?"), min=1, default=1)

    con_quien_vive = models.CharField(
        verbose_name=("¿Con quién vive actualmente?"), max_length=255, default=False)

    cuenta_con_automovil = models.BooleanField(
        verbose_name=("Automóvil propio excluyendo taxis"),
        widget=widgets.RadioSelectHorizontal(), default=False)
    cuantos_automovil = models.PositiveIntegerField(default=0)

    cuenta_con_televisor = models.BooleanField(
        verbose_name=("Televisor"),
        widget=widgets.RadioSelectHorizontal(), default=False)
    cuantos_televisor = models.PositiveIntegerField(default=0)

    cuenta_con_celular = models.BooleanField(
        verbose_name=("Teléfono Celular"),
        widget=widgets.RadioSelectHorizontal(), default=False)
    cuantos_celular = models.PositiveIntegerField(default=0)

    cuenta_con_computadora = models.BooleanField(
        verbose_name=("Computadora de escritorio o portátil"),
        widget=widgets.RadioSelectHorizontal(), default=False)
    cuantos_computadora = models.PositiveIntegerField(default=0)

    cuenta_con_bano = models.BooleanField(
        verbose_name=("Baño completo con regadera y excusado para uso exclusivo del hogar"),
        widget=widgets.RadioSelectHorizontal(), default=False)
    cuantos_bano = models.PositiveIntegerField(default=0)

    cuenta_con_servidumbre = models.BooleanField(
        verbose_name=("Personas de servicio doméstico como limpieza, jardinero o chofer"),
        widget=widgets.RadioSelectHorizontal(), default=False)
    cuantos_servidumbre = models.PositiveIntegerField(default=0)

    tarjeta_de_credito = models.BooleanField(
        verbose_name=("Cuenta usted con tarjeta de crédito"),
        widget=widgets.RadioSelectHorizontal(), default=False)

    altura = models.FloatField(
        verbose_name=("Aproximadamente, ¿qué estatura tiene usted?"),
        min=0, max=2.5, widget=widgets.SliderInput(attrs={'step': '0.1'}), default=0)

    peso = models.PositiveIntegerField(
        verbose_name=("Aproximadamente, ¿qué peso tiene usted? (en kilogramos)"),
        min=0, max=200, widget=widgets.SliderInput(), default=0)

    ejercicio_fisico = models.BooleanField(
        verbose_name=("Durante las últimas dos semanas, ¿ha realizado usted ejercicio físico fuera del trabajo?"),
        widget=widgets.RadioSelectHorizontal(), default=False)

    cigarrillo = models.BooleanField(
        verbose_name=("Durante las últimas dos semanas, ¿ha fumado algún cigarrillo o puro?"),
        widget=widgets.RadioSelectHorizontal(), default=False)

    vive_con_padre = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), default=False)
    vive_con_madre = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), default=False)

    edad_padre = models.PositiveIntegerField(
        choices=range(1, 101), default=1)
    edad_madre = models.PositiveIntegerField(
        choices=range(1, 101), default=1)

    padre_habla_dialecto_indigena = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), default=False)
    madre_habla_dialecto_indigena = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), default=False)

    padre_habla_lengua_extranjera = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), default=False)
    madre_habla_lengua_extranjera = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), default=False)

    nivel_educacion_padre = models.CharField(
        choices=["---", "Primaria", "Secundaria", "Preparatoria", "Universitario"],
        max_length=50, default="---")
    nivel_educacion_madre = models.CharField(
        choices=["---", "Primaria", "Secundaria", "Preparatoria", "Universitario"],
        max_length=50, default="---")

