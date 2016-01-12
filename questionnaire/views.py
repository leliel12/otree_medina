# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

def vars_for_all_templates(self):

    return {}


class Welcome(Page):
    pass


class Bloque1(Page):

    form_model = models.Player
    form_fields = [
        "satisfecho_con_la_vida",
        "cuartos_en_el_hogar", "cuantos_cuartos_se_usan_para_dormir",
        "habitantes",
        "focos",
        "con_quien_vive",
        "cuenta_con_automovil", "cuantos_automovil",
        "cuenta_con_televisor", "cuantos_televisor",
        "cuenta_con_celular", "cuantos_celular",
        "cuenta_con_computadora", "cuantos_computadora",
        "cuenta_con_bano", "cuantos_bano",
        "cuenta_con_servidumbre", "cuantos_servidumbre",
        "tarjeta_de_credito",
        "altura", "peso", "ejercicio_fisico", "cigarrillo",

        "vive_con_padre", "vive_con_madre",
        "edad_padre", "edad_madre",
        "padre_habla_dialecto_indigena", "madre_habla_dialecto_indigena",
        "padre_habla_lengua_extranjera", "madre_habla_lengua_extranjera",
        "nivel_educacion_padre", "nivel_educacion_madre"
    ]


page_sequence = [Welcome, Bloque1]
