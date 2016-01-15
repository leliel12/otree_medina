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
        verbose_name=("¿Con quién vive actualmente?"), max_length=255, default="---",
        choices=["---", "Solo", "Con una pareja", "Con amigos", "Con esposo(a)", "Con familia", "Otro"])

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
        min=0, max=2.5, widget=widgets.SliderInput(attrs={'step': '0.01'}), default=0)

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


    # bloque 2
    riqueza_hogar_14_anios = models.PositiveIntegerField(
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=(
            "Comparando el hogar donde vivía a los 14 años con todos los "
            "hogares actuales de México y usando una escala de 1 a 10, en la "
            "que 1 son los hogares más pobres y 10 son los más ricos, ¿dónde "
            "pondría usted su hogar de ese entonces?"),
        choices=range(1, 11), default=1)

    TRABAJOS = ("---", "Patrón o empleador ", "Trabajador por cuenta propia ",
            "Empleado u obrero del sector público",
            "Empleado u obrero del sector privado", "Servicio Doméstico (por pago)",
            "Quehaceres del hogar (sin pago) ", "Trabajador sin pago ",
            "Fuerzas armadas y del orden")

    padre_trabajaba_14_anios = models.BooleanField(widget=widgets.RadioSelectHorizontal(), default=False)
    madre_trabajaba_14_anios = models.BooleanField(widget=widgets.RadioSelectHorizontal(), default=False)
    padre_ocupacion_14_anios = models.CharField(max_length=255, choices=TRABAJOS, default=TRABAJOS[0])
    madre_ocupacion_14_anios = models.CharField(max_length=255, choices=TRABAJOS, default=TRABAJOS[0])
    padre_trabajo_servicios_medicos_14_anios = models.BooleanField(widget=widgets.RadioSelectHorizontal(), default=False)
    madre_trabajo_servicios_medicos_14_anios = models.BooleanField(widget=widgets.RadioSelectHorizontal(), default=False)

    CON_QUIEN_VIVIA = (
        "---", "Solo con el padre", "Solo con la madre",
        "Con ambos, padre y madre", "Con otra familia", "Otra persona")
    con_quien_vivia_14_anios = models.CharField(
        verbose_name=("Cuando usted tenía alrededor de 14 años ¿con quién vivía?"),
        choices=CON_QUIEN_VIVIA, default=CON_QUIEN_VIVIA[0], max_length=255)

    MUCHO_REGULAR_POCO_NADA = ["---", "Mucho", "Regular", "Poco", "Nada"]
    padre_emocionalmente_cerano_14_anios = models.CharField(
        max_length=20, choices=MUCHO_REGULAR_POCO_NADA, default=MUCHO_REGULAR_POCO_NADA[0])
    madre_emocionalmente_cerano_14_anios = models.CharField(
        max_length=20, choices=MUCHO_REGULAR_POCO_NADA, default=MUCHO_REGULAR_POCO_NADA[0])
    padre_entendia_problemas_14_anios = models.CharField(
        max_length=20, choices=MUCHO_REGULAR_POCO_NADA, default=MUCHO_REGULAR_POCO_NADA[0])
    madre_entendia_problemas_14_anios = models.CharField(
        max_length=20, choices=MUCHO_REGULAR_POCO_NADA, default=MUCHO_REGULAR_POCO_NADA[0])
    padre_actividades_escolares_14_anios = models.CharField(
        max_length=20, choices=MUCHO_REGULAR_POCO_NADA, default=MUCHO_REGULAR_POCO_NADA[0])
    madre_actividades_escolares_14_anios = models.CharField(
        max_length=20, choices=MUCHO_REGULAR_POCO_NADA, default=MUCHO_REGULAR_POCO_NADA[0])
    padre_actividades_tiempo_libre_14_anios = models.CharField(
        max_length=20, choices=MUCHO_REGULAR_POCO_NADA, default=MUCHO_REGULAR_POCO_NADA[0])
    madre_actividades_tiempo_libre_14_anios = models.CharField(
        max_length=20, choices=MUCHO_REGULAR_POCO_NADA, default=MUCHO_REGULAR_POCO_NADA[0])
    padre_reglas_claras_14_anios = models.CharField(
        max_length=20, choices=MUCHO_REGULAR_POCO_NADA, default=MUCHO_REGULAR_POCO_NADA[0])
    madre_reglas_claras_14_anios = models.CharField(
        max_length=20, choices=MUCHO_REGULAR_POCO_NADA, default=MUCHO_REGULAR_POCO_NADA[0])

    relacion_padres_14_anios = models.CharField(
        verbose_name=("¿La relación entre sus padres generalmente era: excelente, buena, regular, mala o muy mala?"),
        max_length=20, default="---",
        choices=["---", "Excelente", "Buena", "Regular", "Mala", "Muy mala"])

    FAMILIA_FRECUENCIA = ("Siempre", "Frecuentemente", "Pocas", "veces", "Nunca", "Omitir")
    familia_frecuencia_insultos_14_anios = models.CharField(
        verbose_name=("¿Con qué frecuencia ocurrían INSULTOS, GRITOS o AMENAZAS en su familia?"),
        max_length=20, choices=FAMILIA_FRECUENCIA, default=FAMILIA_FRECUENCIA[-1])
    familia_frecuencia_cercania_14_anios = models.CharField(
        verbose_name=("¿Con qué frecuencia los miembros de su familia se sentían muy cercanos los unos de los otros?"),
        max_length=20, choices=FAMILIA_FRECUENCIA, default=FAMILIA_FRECUENCIA[-1])
    frequencia_miedos_14_anios = models.CharField(
        verbose_name=("¿Con qué frecuencia lo molestaban miedos o preocupaciones?"),
        max_length=20, choices=FAMILIA_FRECUENCIA, default=FAMILIA_FRECUENCIA[-1])

    madre_trabajo_por_ingreso_desde_que_nacio = models.BooleanField(
        verbose_name=("¿Su madre trabajo por un ingreso en algún momento desde que usted nació hasta el día de hoy?"),
        widget=widgets.RadioSelectHorizontal(), default=False)

    madre_trabajo_periodos_de_su_vida_0_4_anios = models.BooleanField(
        verbose_name=("0 a 4 años de edad"), widget=widgets.RadioSelectHorizontal(), default=False)

    madre_trabajo_periodos_de_su_vida_5_9_anios = models.BooleanField(
        verbose_name=("5 a 9 años de edad"), widget=widgets.RadioSelectHorizontal(), default=False)

    madre_trabajo_periodos_de_su_vida_10_14_anios = models.BooleanField(
        verbose_name=("10 a 14 años de edad"), widget=widgets.RadioSelectHorizontal(), default=False)

    madre_trabajo_periodos_de_su_vida_15_19_anios = models.BooleanField(
        verbose_name=("15 a 19 años de edad"), widget=widgets.RadioSelectHorizontal(), default=False)

    tiene_hermanos = models.BooleanField(
        verbose_name=("¿Tiene usted hermanos o hermanas?"),
        widget=widgets.RadioSelectHorizontal(), default=False)

    numero_de_hermano_que_es_usted = models.PositiveIntegerField(
        verbose_name=(
            "Ahora piense en sus hermanos ordenándolos del mayor al menor "
            "aunque hayan fallecido y dígame qué número de hermano es usted."),
        choices=range(1, 11), default=1, widget=widgets.RadioSelectHorizontal())

    HERMANOS_1_10 = ["---"] + [str(i) for i in range(1, 11)]
    hermanos_que_son = models.CharField(choices=HERMANOS_1_10, max_length=10, default=HERMANOS_1_10[0])
    hermanas_que_son = models.CharField(choices=HERMANOS_1_10, max_length=10, default=HERMANOS_1_10[0])
    hermanos_viven_con_usted_actualmente = models.CharField(choices=HERMANOS_1_10, max_length=10, default=HERMANOS_1_10[0])
    hermanas_viven_con_usted_actualmente = models.CharField(choices=HERMANOS_1_10, max_length=10, default=HERMANOS_1_10[0])
    hermanos_trabajan_por_pago_actualmente = models.CharField(choices=HERMANOS_1_10, max_length=10, default=HERMANOS_1_10[0])
    hermanas_trabajan_por_pago_actualmente = models.CharField(choices=HERMANOS_1_10, max_length=10, default=HERMANOS_1_10[0])

    espera_trabajar_remonerado_mayor_parte_de_su_vida = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=("¿Espera usted trabajar de forma remunerada la mayor parte de su vida?"), default=False)

    TRABAJO_FUTURO = [
        "---", "Asalariado", "Auto-empleado", "Dueño de negocio",
        "Dueño de empresa", "Ninguna de las anteriores"]
    de_que_manera_espera_trabajar = models.CharField(
        verbose_name="¿De qué manera espera trabajar?",
        choices=TRABAJO_FUTURO, max_length=100, default=TRABAJO_FUTURO[0])

    cuanto_cree_que_ganaria_en_30_anios = models.PositiveIntegerField(
        verbose_name=(
            "Imagine que usted tiene 30 años el día de hoy y está trabajando "
            "de forma remunerada. ¿Cuánto cree que ganaría al mes por su trabajo?"), default=0)

    cree_que_tendra_hijo = models.CharField(
        verbose_name="Cree que usted tenga un hijo en algún momento de la vida?",
        choices=["---", "Si", "No", "Ya lo tuvo"], max_length=100, default="---")

    edad_de_primer_hijo = models.PositiveIntegerField(
        verbose_name=("¿A qué edad espera tener su primer hijo?"), choices=range(1, 100), default=0)

    edad_tuvo_primer_hijo = models.PositiveIntegerField(
        verbose_name=("¿A qué edad tuvo a su primer hijo?"), choices=range(1, 100), default=0)

    # BLOQUE 3
    RANGO_1_10 = range(1, 11)

    hogar_actual_vs_mexico = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))

    cuanto_depende_de_usted_que_le_vaya_bien = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))

    gobierno_o_sociedad_pobreza = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    gobierno_o_sociedad_delincuencia = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    gobierno_o_sociedad_narcotrafico = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    gobierno_o_sociedad_corrupcion = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    gobierno_o_sociedad_educacion = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    gobierno_o_sociedad_discriminacion = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    gobierno_o_sociedad_adicciones_y_enfermedades = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))

    dispuesto_a_tomar_riesgos = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))

    describe_como_persona_abstengo_hacer_cosas_hoy = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    describe_como_persona_retrazo_cosas = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    describe_como_persona_asumo_gente_tiene_mejores_intenciones = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    describe_como_persona_no_entiendo_gente_pelea_causa_que_no_le_beneficia = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    describe_como_persona_ayudo_al_que_me_ayudo = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    describe_como_persona_me_vengo = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))

    que_tan_impulsivo_se_considera = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))

    dispuesto_a_confiar = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    dispuesto_a_compartir = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    dispuesto_a_regresar_favor = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    dispuesto_a_castigar = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))

    que_tan_paciente_se_considera = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))

    acuerdo_con_educacion_genera_ingreso = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_hombres_mas_trabajo_que_mujeres = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_esposa_que_gana_mas_genera_dinero = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_no_se_puede_confiar_en_nadie = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_camino_de_mi_vida = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_he_logrado_lo_que_merezco = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_logros_suerte = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_otros_deciden_por_mi = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_puedo_influir_en_condicion_social = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_trabajar_duro_exito = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_dudo_de_mi_mismo = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_oportunidades_dadas_por_condiciones_sociales = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_habilidades_mas_que_esfuerzo = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))
    acuerdo_con_poco_control_de_la_vida = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        verbose_name=(""))




