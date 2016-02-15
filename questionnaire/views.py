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
        "block_1_last_question_clicked",

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
    timeout_seconds = 3 * 60 + 30

    form_model = models.Player
    form_fields = [
        "block_2_last_question_clicked",

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


class Bloque3(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 5 * 60

    form_model = models.Player
    form_fields = [
        "block_3_last_question_clicked",

        "hogar_actual_vs_mexico",

        "cuanto_depende_de_usted_que_le_vaya_bien",

        "gobierno_o_sociedad_pobreza", "gobierno_o_sociedad_delincuencia",
        "gobierno_o_sociedad_narcotrafico", "gobierno_o_sociedad_corrupcion",
        "gobierno_o_sociedad_educacion", "gobierno_o_sociedad_discriminacion",
        "gobierno_o_sociedad_adicciones_y_enfermedades",

        "dispuesto_a_tomar_riesgos",

        "describe_como_persona_abstengo_hacer_cosas_hoy",
        "describe_como_persona_retrazo_cosas",
        "describe_como_persona_asumo_gente_tiene_mejores_intenciones",
        "describe_como_persona_no_entiendo_pelea_no_le_beneficia",
        "describe_como_persona_ayudo_al_que_me_ayudo",
        "describe_como_persona_me_vengo",

        "que_tan_impulsivo_se_considera",

        "dispuesto_a_confiar", "dispuesto_a_compartir",
        "dispuesto_a_regresar_favor", "dispuesto_a_castigar",

        "que_tan_paciente_se_considera",

        "acuerdo_con_educacion_genera_ingreso",
        "acuerdo_con_hombres_mas_trabajo_que_mujeres",
        "acuerdo_con_esposa_que_gana_mas_genera_dinero",
        "acuerdo_con_no_se_puede_confiar_en_nadie",
        "acuerdo_con_camino_de_mi_vida",
        "acuerdo_con_he_logrado_lo_que_merezco",
        "acuerdo_con_logros_suerte", "acuerdo_con_otros_deciden_por_mi",
        "acuerdo_con_puedo_influir_en_condicion_social",
        "acuerdo_con_trabajar_duro_exito", "acuerdo_con_dudo_de_mi_mismo",
        "acuerdo_con_oportunidades_dadas_por_condiciones_sociales",
        "acuerdo_con_habilidades_mas_que_esfuerzo", "acuerdo_con_poco_control_de_la_vida",

        "que_tanto_es_es_reservado", "que_tanto_es_confiable", "que_tanto_es_flojo",
        "que_tanto_es_relajado", "que_tanto_es_artista", "que_tanto_es_sociable",
        "que_tanto_es_falla_en_los_demas", "que_tanto_es_nervioso",
        "que_tanto_es_imaginador",

        "que_tanto_lo_describe_ideas_me_distraen",
        "que_tanto_lo_describe_contratiempos_desanima",
        "que_tanto_lo_describe_persona_trabajadora",
        "que_tanto_lo_describe_pierdo_interes",
        "que_tanto_lo_describe_persigo_diferentes_metas",
        "que_tanto_lo_describe_dificultades_para_concentracion",
        "que_tanto_lo_describe_termino_lo_que_comienzo",
        "que_tanto_lo_describe_efuerzo_en_mi_trabajo",
        "que_tanto_lo_describe_malos_habitos",
        "que_tanto_lo_describe_cosas_inapropiadas",
        "que_tanto_lo_describe_resisto_tentaciones",
        "que_tanto_lo_describe_me_arrepiento",
        "que_tanto_lo_describe_hago_cosas_sin_pensar",

        "apuesta_loteria_1000",

        "donar_1000",

        "pagan_100_esperar_3_meses",
        "que_tanto_lo_describe_1_anio"]


class Bloque4Mujeres(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 3 * 60

    form_model = models.Player
    form_fields = [
        "block_4_last_question_clicked",

        "mestruando",
        "fecha_ultima_regla",
        "fecha_siguiente_regla",
        "anticonceptivos",
        "duracion_del_sangrado",
    ]

    def is_displayed(self):
        return self.player.genero == Constants.mujer


class Bloque4Hombres(TimeOutMixin, Page):

    process_form_on_timeout = True
    #~ timeout_seconds = 3 * 60

    form_model = models.Player
    form_fields = [
        "block_4_last_question_clicked",
        "trabaja_empresa_dependencia_publica",
        "fecha_busqueda_empleo",
        "fecha_fin_de_estudios",
        "discriminacion_laboral",
        "que_tanto_presencio_discriminacion",
    ]

    def is_displayed(self):
        return self.player.genero == Constants.hombre


class Bloque5(TimeOutMixin, Page):

    process_form_on_timeout = True
    timeout_seconds = 4 * 60

    form_model = models.Player
    form_fields = [
        "fig1", "fig2", "fig3", "fig4", "fig5",
        "fig6", "fig7", "fig8", "fig9", "fig10"]


page_sequence = [
    Welcome, Bloque1, Bloque2, Bloque3,
    Bloque4Mujeres, Bloque4Hombres,
    Bloque5]
