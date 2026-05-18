from services.buscador_faq import hay_contexto_disponible, normalizar_texto, obtener_contexto_local
from services.groq_service import preguntar_a_llama

# Configuracion principal del asistente.
# Para adaptar este proyecto a otro cliente, cambia estos valores:
# - Consultorio odontologico: "Asistente Virtual Consultorio Dental"
# - Institucion educativa: "Asistente Virtual Colegio San Jose"
# - Alcaldia/municipio: "Asistente Virtual Alcaldia"
NOMBRE_ASISTENTE = "Asistente Virtual Alcaldia"

# Lista de temas que el bot puede mencionar cuando el ciudadano hace una
# pregunta muy general o cuando no hay informacion suficiente en las FAQs.
# Manten esta lista alineada con el contenido real de data/faqs.csv.
TEMAS_DISPONIBLES = [
    "impuesto predial",
    "recoleccion de aseo",
    "reporte de huecos o luminarias danadas",
    "citas del Sisben",
]

PREGUNTAS_GENERALES = [
    "que servicios",
    "que puedo consultar",
    "como me puede ayudar",
    "en que me puedes ayudar",
    "en que me puede ayudar",
    "que haces",
    "que sabes",
]

DATOS_INSTITUCIONALES = [
    "direccion",
    "ubicacion",
    "ubicada",
    "ubicado",
    "telefono",
    "nit",
    "ciudad",
    "horario de atencion",
    "sede",
]


def construir_menu_temas():
    temas = "\n".join(f"- {tema}" for tema in TEMAS_DISPONIBLES)
    return (
        "Puedo orientarte sobre la informacion que tengo cargada actualmente:\n"
        f"{temas}\n\n"
        "Sobre cual tema necesitas ayuda?"
    )


def construir_respuesta_sin_contexto():
    temas = "\n".join(f"- {tema}" for tema in TEMAS_DISPONIBLES)
    return (
        "No tengo esa informacion en la base de conocimiento disponible. "
        "Actualmente puedo orientarte sobre:\n"
        f"{temas}"
    )


def es_pregunta_general(pregunta):
    pregunta_normalizada = normalizar_texto(pregunta)
    return any(frase in pregunta_normalizada for frase in PREGUNTAS_GENERALES)


def pide_dato_institucional(pregunta):
    pregunta_normalizada = normalizar_texto(pregunta)
    return any(dato in pregunta_normalizada for dato in DATOS_INSTITUCIONALES)


def generar_respuesta(entrada):
    if es_pregunta_general(entrada):
        return construir_menu_temas()

    if pide_dato_institucional(entrada):
        return construir_respuesta_sin_contexto()

    contexto_encontrado = obtener_contexto_local(entrada)
    if not hay_contexto_disponible(contexto_encontrado):
        return construir_respuesta_sin_contexto()

    return preguntar_a_llama(entrada, contexto_encontrado)


def iniciar_chat():
    print(f"[{NOMBRE_ASISTENTE}] En linea. Escribe 'salir' para terminar.\n")

    while True:
        entrada = input("Ciudadano: ")
        if entrada.lower() == "salir":
            print("Bot: Que tenga un excelente dia. Hasta luego!")
            break

        respuesta_ia = generar_respuesta(entrada)
        print(f"Bot: {respuesta_ia}\n")


if __name__ == "__main__":
    iniciar_chat()
