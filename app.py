from services.buscador_faq import obtener_contexto_local
from services.groq_service import preguntar_a_llama


def iniciar_chat():
    print("[Asistente Virtual Alcaldia] En linea. Escribe 'salir' para terminar.\n")

    while True:
        entrada = input("Ciudadano: ")
        if entrada.lower() == "salir":
            print("Bot: Que tenga un excelente dia. Hasta luego!")
            break

        contexto_encontrado = obtener_contexto_local(entrada)
        respuesta_ia = preguntar_a_llama(entrada, contexto_encontrado)

        print(f"Bot: {respuesta_ia}\n")


if __name__ == "__main__":
    iniciar_chat()
