from services.buscador_faq import buscar_faqs_relevantes, obtener_contexto_local


def primera_pregunta_encontrada(consulta):
    resultados = buscar_faqs_relevantes(consulta, max_resultados=1)
    assert resultados, f"No se encontraron FAQs para: {consulta}"
    return resultados[0]["pregunta"]


def test_encuentra_horario_del_aseo_con_sinonimos():
    pregunta = primera_pregunta_encontrada("a que hora pasa el auto del aseo")

    assert "Hora de pasada" in pregunta


def test_encuentra_dias_de_recoleccion_con_pregunta_no_literal():
    pregunta = primera_pregunta_encontrada("cuando recogen los residuos")

    assert "Dias en que pasa" in pregunta


def test_encuentra_predial_con_factura():
    pregunta = primera_pregunta_encontrada("necesito bajar la factura predial")

    assert "impuesto predial" in pregunta


def test_encuentra_reporte_de_luminaria():
    pregunta = primera_pregunta_encontrada("como aviso que hay una lampara rota")

    assert "luminaria" in pregunta


def test_contexto_indica_sin_informacion_si_no_hay_coincidencia():
    contexto = obtener_contexto_local("quiero renovar mi pasaporte")

    assert "No hay informacion especifica" in contexto
