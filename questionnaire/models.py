# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division, unicode_literals
from otree.db import models
import otree.models
from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>

from django.utils import timezone

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
    mujer = "Mujer"
    hombre = "Hombre"


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

    player_name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)

    genero = models.CharField(
        max_length=30, widget=widgets.RadioSelectHorizontal(),
        choices=[Constants.hombre, Constants.mujer], verbose_name="Seleccióne su género")

    # bloque 1
    block_1_last_question_clicked = models.IntegerField(default=0, widget=widgets.HiddenInput())

    satisfecho_con_la_vida = models.PositiveIntegerField(
        verbose_name=(
            "En una escala del 1 al 10, donde 1 es nada satisfecho y 10 "
            "totalmente satisfecho, en general ¿qué tan satisfecha(o) se "
            "encuentra usted con su vida? Usted puede escoger cualquier "
            "número entre 1 y 10."), choices=range(1,11),
            widget=widgets.RadioSelectHorizontal(), default=1)

    cuartos_en_el_hogar = models.PositiveIntegerField(
        widget=widgets.SliderInput(), max=20,
        verbose_name=("¿Cuántos cuartos hay en su hogar sin contar pasillos, ni baños?"), min=1, default=1)

    cuantos_cuartos_se_usan_para_dormir = models.PositiveIntegerField(
        widget=widgets.SliderInput(), max=20,
        verbose_name=("Y de esos cuartos, ¿cuántos usan para dormir?"), min=1, default=1)

    habitantes = models.PositiveIntegerField(
        widget=widgets.SliderInput(), max=20,
        verbose_name=("¿Cuántas personas viven en su hogar contando ancianos y niños?"), min=1, default=1)

    focos = models.PositiveIntegerField(
        widget=widgets.SliderInput(), max=50,
        verbose_name=(
            "Contando todos los focos que utiliza para iluminar su hogar, "
            "incluyendo los de techos, paredes y lámparas de buró o piso, "
            "dígame, ¿Cuántos focos tiene en su vivienda?"), min=1, default=1)

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
        verbose_name=("Aproximadamente, ¿qué estatura tiene usted? (en metros)"),
        min=0, widget=widgets.SliderInput(attrs={'step': '0.01', 'max': '2.5'}), default=0)

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
        choices=range(30, 101), default=30)
    edad_madre = models.PositiveIntegerField(
        choices=range(30, 101), default=30)

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
    block_2_last_question_clicked = models.IntegerField(default=0, widget=widgets.HiddenInput())

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

    FAMILIA_FRECUENCIA = ("Siempre", "Frecuentemente", "Pocas veces", "Nunca", "Omitir")
    familia_frecuencia_insultos_14_anios = models.CharField(
        verbose_name=("¿Con qué frecuencia ocurrían INSULTOS, GRITOS o AMENAZAS en su familia?"),
        max_length=20, choices=FAMILIA_FRECUENCIA, default=FAMILIA_FRECUENCIA[-1])
    familia_frecuencia_cercania_14_anios = models.CharField(
        verbose_name=("¿Con qué frecuencia los miembros de su familia se sentían muy cercanos los unos de los otros?"),
        max_length=20, choices=FAMILIA_FRECUENCIA, default=FAMILIA_FRECUENCIA[-1])
    frequencia_miedos_14_anios = models.CharField(
        verbose_name=("¿Con qué frecuencia la/lo molestaban miedos o preocupaciones?"),
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
        widget=widgets.SliderInput(), max=100000,
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
    block_3_last_question_clicked = models.IntegerField(default=0, widget=widgets.HiddenInput())

    RANGO_1_10 = range(1, 11)

    hogar_actual_vs_mexico = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Comparando su hogar actual con todos los hogares actuales de México y usando una escala de 1 a 10, en la que 1 son los hogares más pobres y 10 son los más ricos, ¿dónde pondría usted su hogar actual?"))

    cuanto_depende_de_usted_que_le_vaya_bien = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("En una escala del 1 al 10, donde 1 es “nada depende de usted” y 10 es “todo depende de usted”, ¿qué tanto depende de usted misma(o) que le vaya bien en este año y el próximo?"))

    gobierno_o_sociedad_pobreza = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        widget=widgets.RadioSelectHorizontal(), verbose_name=("Pobreza"))
    gobierno_o_sociedad_delincuencia = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        widget=widgets.RadioSelectHorizontal(), verbose_name=("Delincuencia"))
    gobierno_o_sociedad_narcotrafico = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        widget=widgets.RadioSelectHorizontal(), verbose_name=("Narcotráfico"))
    gobierno_o_sociedad_corrupcion = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        widget=widgets.RadioSelectHorizontal(), verbose_name=("Corrupción"))
    gobierno_o_sociedad_educacion = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        widget=widgets.RadioSelectHorizontal(), verbose_name=("Mala o Poca Educación"))
    gobierno_o_sociedad_discriminacion = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        widget=widgets.RadioSelectHorizontal(), verbose_name=("Discriminación"))
    gobierno_o_sociedad_adicciones_y_enfermedades = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0],
        widget=widgets.RadioSelectHorizontal(), verbose_name=("Atención de adicciones y enfermedades"))

    dispuesto_a_tomar_riesgos = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("En una escala del 1 al 10, donde 1 es nada dispuesto y 10 totalmente dispuesto, ¿qué tan dispuesto está a tomar riesgos?"))

    describe_como_persona_abstengo_hacer_cosas_hoy = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Me abstengo de cosas hoy para poder tener más mañana"))
    describe_como_persona_retrazo_cosas = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Tiendo a retrasar cosas aun cuando sería mejor hacerlas de una vez"))
    describe_como_persona_asumo_gente_tiene_mejores_intenciones = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Mientras no esté convencido de lo contrario, siempre asumo que la gente tiene las mejores intenciones"))
    describe_como_persona_no_entiendo_pelea_no_le_beneficia = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("No entiendo por qué alguna gente dedica su vida a pelear por una causa que no les beneficia directamente"))
    describe_como_persona_ayudo_al_que_me_ayudo = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Realizo un gran esfuerzo para ayudar a alguien que me ha ayudado antes"))
    describe_como_persona_me_vengo = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Si alguien me hace algo malo a propósito, trataré de regresárselo"))

    que_tan_impulsivo_se_considera = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("En una escala del 1 al 10, donde 1 es totalmente y 10 es nada, ¿qué tan impulsivo se considera?"))

    dispuesto_a_confiar = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Confiar en otras personas"))
    dispuesto_a_compartir = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Compartir algo con otras personas sin nada a cambio"))
    dispuesto_a_regresar_favor = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Regresar un favor a un extraño"))
    dispuesto_a_castigar = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Castigar a alguien debido a una conducta injusta aun cuando es costoso. Ej. Decirle a una persona que no tire basura en la calle aun cuando esa persona se puede enojar y decirle algo."))

    que_tan_paciente_se_considera = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("En una escala del 1 al 10, donde 1 es muy paciente y 10 es muy impaciente, ¿qué tan paciente o impaciente se considera? Usted puede escoger cualquier número entre 1 y 10."))

    acuerdo_con_educacion_genera_ingreso = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("El nivel educativo determina el nivel de ingreso de una persona"))
    acuerdo_con_hombres_mas_trabajo_que_mujeres = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Cuando no hay mucho trabajo, los hombres deberían de tener preferencia a un trabajo antes que las mujeres"))
    acuerdo_con_esposa_que_gana_mas_genera_dinero = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("La esposa que gana más dinero que el esposo genera problemas"))
    acuerdo_con_no_se_puede_confiar_en_nadie = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Hoy en día, no se puede confiar en nadie más"))
    acuerdo_con_camino_de_mi_vida = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("El camino de mi vida depende de mí"))
    acuerdo_con_he_logrado_lo_que_merezco = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("En comparación con otros, no he logrado lo que merezco"))
    acuerdo_con_logros_suerte = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Lo que se logra en la vida es principalmente una cuestión de destino o suerte"))
    acuerdo_con_otros_deciden_por_mi = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Frecuentemente tengo la sensación de que otros toman decisiones sobre mi vida"))
    acuerdo_con_puedo_influir_en_condicion_social = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Si uno es social o políticamente activo, se puede influir en las condiciones sociales"))
    acuerdo_con_trabajar_duro_exito = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Hay que trabajar duro para alcanzar el éxito"))
    acuerdo_con_dudo_de_mi_mismo = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Si enfrento dificultades en la vida, frecuentemente dudo de mí mismo"))
    acuerdo_con_oportunidades_dadas_por_condiciones_sociales = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Las oportunidades que tengo en la vida están determinadas por las condiciones sociales"))
    acuerdo_con_habilidades_mas_que_esfuerzo = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Las habilidades con las que nací son más importantes que todo el esfuerzo que yo pueda hacer"))
    acuerdo_con_poco_control_de_la_vida = models.PositiveIntegerField(
        choices=RANGO_1_10, default=RANGO_1_10[0], widget=widgets.RadioSelectHorizontal(),
        verbose_name=("Tengo poco control sobre las cosas que suceden en mi vida"))

    TOTALMENTE_MUCHO_REGULAR_POCO_NADA = ("---", "Totalmente", "Mucho", "Regular", "Poco", "Nada")
    que_tanto_es_es_reservado = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Es reservado(a)"))
    que_tanto_es_confiable = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Es generalmente confiable"))
    que_tanto_es_flojo = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Tiende a ser flojo(a)"))
    que_tanto_es_relajado = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Es relajado(a) o maneja bien el estrés"))
    que_tanto_es_artista = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Tiene intereses artísticos"))
    que_tanto_es_sociable = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Es extrovertido(a) o sociable"))
    que_tanto_es_falla_en_los_demas = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Tiende a encontrar fallas en los demás"))
    que_tanto_es_nervioso = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Se pone nervioso(a) fácilmente"))
    que_tanto_es_imaginador = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Tiene una imaginación activa"))

    que_tanto_lo_describe_ideas_me_distraen = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Algunas veces nuevas ideas y proyectos me distraen de mis proyectos e ideas anteriores"))
    que_tanto_lo_describe_contratiempos_desanima = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Los contratiempos no me desaniman"))
    que_tanto_lo_describe_persona_trabajadora = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Soy una persona muy trabajadora"))
    que_tanto_lo_describe_pierdo_interes = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Me obsesiono con ideas o proyectos por un tiempo, pero pierdo el interés rápidamente."))
    que_tanto_lo_describe_persigo_diferentes_metas = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Frecuentemente me pongo una meta pero más tarde persigo una diferente."))
    que_tanto_lo_describe_dificultades_para_concentracion = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Tengo dificultades para mantener mi concentración en proyectos que toman más de unos cuantos meses en completarse."))
    que_tanto_lo_describe_termino_lo_que_comienzo = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Termino todo lo que comienzo"))
    que_tanto_lo_describe_efuerzo_en_mi_trabajo = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Pongo mucho esfuerzo en los trabajos que realizo"))
    que_tanto_lo_describe_malos_habitos = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Me cuesta romper malos hábitos"))
    que_tanto_lo_describe_cosas_inapropiadas = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Frecuentemente digo cosas inapropiadas"))
    que_tanto_lo_describe_resisto_tentaciones = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Soy muy bueno para resistir tentaciones"))
    que_tanto_lo_describe_me_arrepiento = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Hago cosas que se sienten bien en el momento pero después me arrepiento de ellas"))
    que_tanto_lo_describe_hago_cosas_sin_pensar = models.CharField(
        choices=TOTALMENTE_MUCHO_REGULAR_POCO_NADA, default=TOTALMENTE_MUCHO_REGULAR_POCO_NADA[0],
        max_length=30, verbose_name=("Frecuentemente hago cosas sin pensar en todas las opciones"))

    apuesta_loteria_1000 = models.PositiveIntegerField(
        verbose_name=("Imagine un juego de lotería con diez boletos numerados del 1 al 10, cuyo premio al número ganador es de $1,000. ¿Cuánto estaría dispuesto a pagar por un boleto para participar en ella?"),
        min=0, max=1000, widget=widgets.SliderInput(), default=0)

    donar_1000 = models.PositiveIntegerField(
        verbose_name=("Imagine la siguiente situación: El día de hoy usted recibe inesperadamente $1,000. ¿Cuánto consideraría donar a una buena causa?"),
        min=0, max=1000, widget=widgets.SliderInput(), default=0)

    pagan_100_esperar_3_meses = models.PositiveIntegerField(
        min=1000, max=50000,  widget=widgets.SliderInput(),
        verbose_name=("¿Cuánto le tendrían que pagar dentro de tres meses para que pueda esperar este tiempo?"), default=0)
    que_tanto_lo_describe_1_anio = models.PositiveIntegerField(
        min=1000, max=50000,  widget=widgets.SliderInput(),
        verbose_name=("Y ahora, ¿cuánto le tendrían que pagar dentro de un año para que pueda esperar ese tiempo?"), default=0)

    # bloque 4
    block_4_last_question_clicked = models.IntegerField(default=0, widget=widgets.HiddenInput())

    # MUJERES
    mestruando = models.BooleanField(
        verbose_name="¿Se encuentra usted menstruando el día de hoy?", default=False, widget=widgets.RadioSelectHorizontal())

    fecha_ultima_regla = models.DateField(
        default=lambda: timezone.now().date(),
        verbose_name="Fecha de comienzo de última regla (si no recuerda con precisión, favor de indicar la fecha más próxima).")
    fecha_siguiente_regla = models.DateField(
        default=lambda: timezone.now().date(),
        verbose_name="Fecha esperada de comienzo de siguiente regla (si no puede calcular con precisión, favor de indicar la fecha más próxima independientemente de si usted es regular o irregular)")

    anticonceptivos = models.BooleanField(
        verbose_name="¿Utiliza pastillas anticonceptivas?", default=False, widget=widgets.RadioSelectHorizontal())

    duracion_del_sangrado = models.PositiveIntegerField(
        verbose_name=("¿Normalmente, cuántos días dura el sangrado?"),
        widget=widgets.SliderInput(), default=5, min=1, max=10)

    # HOMBRES
    trabaja_empresa_dependencia_publica = models.BooleanField(
        verbose_name="Actualmente se encuentra trabajando en alguna empresa o dependencia pública?",
        default=False, widget=widgets.RadioSelectHorizontal())

    fecha_busqueda_empleo = models.DateField(
        default=lambda: timezone.now().date(),
        verbose_name="Aproximadamente, cuando fue la última fecha en que buscó empleo?.")
    fecha_fin_de_estudios  = models.DateField(
        default=lambda: timezone.now().date(),
        verbose_name="Fecha en la que dio por terminados sus estudios?")

    discriminacion_laboral = models.BooleanField(
        verbose_name="Desde su perspectiva, alguna vez ha sido victima de discriminación laboral?",
        default=False, widget=widgets.RadioSelectHorizontal())

    que_tanto_presencio_discriminacion = models.PositiveIntegerField(
        verbose_name=("En una escala del 1 al 10, que tanto ha presenciado discriminación, para usted o algún compañero, en el campo laboral?"),
        widget=widgets.SliderInput(), default=5, min=1, max=10)


    # Bloque 5
    FIGURE_CHOICES_6 = ['---', '1', '2', '3', '4', '5', '6']

    fig1 = models.CharField(
        verbose_name="fig1.jpg",
        max_length=10, choices=FIGURE_CHOICES_6, default=FIGURE_CHOICES_6[0])
    fig2 = models.CharField(
        verbose_name="fig2.jpg",
        max_length=10, choices=FIGURE_CHOICES_6, default=FIGURE_CHOICES_6[0])
    fig3 = models.CharField(
        verbose_name="fig3.jpg",
        max_length=10, choices=FIGURE_CHOICES_6, default=FIGURE_CHOICES_6[0])
    fig4 = models.CharField(
        verbose_name="fig4.jpg",
        max_length=10, choices=FIGURE_CHOICES_6, default=FIGURE_CHOICES_6[0])

    FIGURE_CHOICES_8 = ['---', '1', '2', '3', '4', '5', '6', '7', '8']
    fig5 = models.CharField(
        verbose_name="fig5.jpg",
        max_length=10, choices=FIGURE_CHOICES_8, default=FIGURE_CHOICES_8[0])
    fig6 = models.CharField(
        verbose_name="fig6.jpg",
        max_length=10, choices=FIGURE_CHOICES_8, default=FIGURE_CHOICES_8[0])
    fig7 = models.CharField(
        verbose_name="fig7.jpg",
        max_length=10, choices=FIGURE_CHOICES_8, default=FIGURE_CHOICES_8[0])
    fig8 = models.CharField(
        verbose_name="fig8.jpg",
        max_length=10, choices=FIGURE_CHOICES_8, default=FIGURE_CHOICES_8[0])
    fig9 = models.CharField(
        verbose_name="fig9.jpg",
        max_length=10, choices=FIGURE_CHOICES_8, default=FIGURE_CHOICES_8[0])
    fig10 = models.CharField(
        verbose_name="fig10.jpg",
        max_length=10, choices=FIGURE_CHOICES_8, default=FIGURE_CHOICES_8[0])









