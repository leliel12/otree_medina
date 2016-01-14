# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

from utils import TimeOutMixin

def vars_for_all_templates(self):

    return {}


class Welcome(Page):
    pass


class Bloque1(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 3 * 60

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


class Bloque2(TimeOutMixin, Page):

    process_form_on_timeout = True
    #~ timeout_seconds = 3 * 60

    form_model = models.Player
    form_fields = [
        "riqueza_hogar_14_anios",

        "padre_trabajaba_14_anios", "madre_trabajaba_14_anios",
        "padre_ocupacion_14_anios", "madre_ocupacion_14_anios",
        "padre_trabajo_servicios_medicos_14_anios", "madre_trabajo_servicios_medicos_14_anios",

        "con_quien_vivia_14_anios",

        "padre_emocionalmente_cerano_14_anios", "madre_emocionalmente_cerano_14_anios",
        "padre_entendia_problemas_14_anios", "madre_entendia_problemas_14_anios",
        "padre_actividades_escolares_14_anios", "madre_actividades_escolares_14_anios",
        "padre_actividades_tiempo_libre_14_anios", "madre_actividades_tiempo_libre_14_anios",
        "padre_reglas_claras_14_anios", "madre_reglas_claras_14_anios",

         "relacion_padres_14_anios",

         "familia_frecuencia_insultos_14_anios",
         "familia_frecuencia_cercania_14_anios",
         "frequencia_miedos_14_anios",

         "madre_trabajo_por_ingreso_desde_que_nacio",

         "madre_trabajo_periodos_de_su_vida_0_4_anios",
         "madre_trabajo_periodos_de_su_vida_5_9_anios",
         "madre_trabajo_periodos_de_su_vida_10_14_anios",
         "madre_trabajo_periodos_de_su_vida_15_19_anios",

         "tiene_hermanos",

         "numero_de_hermano_que_es_usted",

         "hermanos_que_son", "hermanas_que_son",
         "hermanos_viven_con_usted_actualmente", "hermanas_viven_con_usted_actualmente",
         "hermanos_trabajan_por_pago_actualmente", "hermanas_trabajan_por_pago_actualmente",

         "espera_trabajar_remonerado_mayor_parte_de_su_vida",

         "de_que_manera_espera_trabajar",

         "cuanto_cree_que_ganaria_en_30_anios",

         "cree_que_tendra_hijo",
         "edad_de_primer_hijo",
         "edad_tuvo_primer_hijo"
    ]


page_sequence = [Welcome, Bloque1, Bloque2]
