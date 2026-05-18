# Chatbot Alcaldia

Laboratorio practico de un asistente virtual para atencion ciudadana en alcaldias y municipios.

El proyecto usa Python, un archivo de preguntas frecuentes en CSV y Groq para generar respuestas con un modelo de lenguaje. Antes de llamar al modelo, el sistema busca FAQs relevantes con una capa local de recuperacion flexible para entender preguntas no literales.

## Estructura

```text
app.py
data/
  faqs.csv
services/
  buscador_faq.py
  groq_service.py
tests/
  test_buscador_faq.py
.env.example
.gitignore
README.md
```

## Configuracion

Crea un archivo `.env` en la raiz del proyecto:

```env
GROQ_API_KEY=gsk_tu_clave_real
```

El archivo `.env` no se debe subir a GitHub. Para eso esta incluido en `.gitignore`.

## Ejecutar

```powershell
.venv\Scripts\activate
python app.py
```

## Probar Busqueda Local

Las pruebas validan que el buscador encuentre la FAQ correcta aunque el ciudadano pregunte con otras palabras:

```powershell
pytest
```

Ejemplos que debe entender:

- `a que hora pasa el auto del aseo`
- `cuando recogen los residuos`
- `necesito bajar la factura predial`
- `como aviso que hay una lampara rota`

## Objetivo De Aprendizaje

Este laboratorio simula una necesidad real de un AI Engineer Junior: construir un chatbot que no dependa de coincidencias literales, separe responsabilidades del codigo y pueda crecer hacia FastAPI, Streamlit y RAG.
