import json
import os
from datetime import datetime

EMOCIONES_PATH = "data/emociones.json"

def analizar_emocion(texto):
    """Analiza el texto e identifica la emoción predominante."""
    emociones = {
        "feliz": ["contento", "alegre", "bien", "genial", "fantástico"],
        "triste": ["triste", "deprimido", "mal", "desanimado"],
        "enojado": ["molesto", "enojado", "furioso", "irritado"],
        "ansioso": ["nervioso", "preocupado", "ansioso", "inquieto"]
    }

    for emocion, palabras in emociones.items():
        if any(palabra in texto.lower() for palabra in palabras):
            guardar_historial_emocion(emocion)  # Guardar en historial
            return emocion
    return "neutral"

def responder_emocion(emocion):
    """Devuelve una respuesta adaptada a la emoción detectada."""
    respuestas = {
        "feliz": ["¡Me alegra saber que te sientes bien! 😊", "¡Eso es genial! Sigue disfrutando."],
        "triste": ["Lamento que te sientas así. ¿Quieres hablar de ello?", "Estoy aquí para escucharte."],
        "enojado": ["Parece que estás molesto. ¿Hay algo en lo que pueda ayudar?", "Respira profundo, todo mejorará."],
        "ansioso": ["La ansiedad es difícil, pero estás haciendo lo mejor que puedes.", "Trata de respirar lentamente. Estoy aquí contigo."],
        "neutral": ["Cuéntame más sobre cómo te sientes."],
    }

    return respuestas.get(emocion, ["No sé cómo responder a eso."])[0]

def guardar_historial_emocion(emocion):
    """Guarda la emoción detectada para generar tendencias futuras."""
    if not os.path.exists("data"):
        os.makedirs("data")

    try:
        with open(EMOCIONES_PATH, "r", encoding="utf-8") as file:
            historial = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        historial = []

    entrada = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "emocion": emocion
    }

    historial.append(entrada)

    with open(EMOCIONES_PATH, "w", encoding="utf-8") as file:
        json.dump(historial, file, indent=4, ensure_ascii=False)

def obtener_tendencias_emocionales():
    """Analiza el historial y da recomendaciones basadas en emociones previas."""
    try:
        with open(EMOCIONES_PATH, "r", encoding="utf-8") as file:
            historial = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return "No hay suficientes datos para detectar tendencias."

    conteo = {}
    for entry in historial:
        emocion = entry["emocion"]
        conteo[emocion] = conteo.get(emocion, 0) + 1

    if not conteo:
        return "No hay datos suficientes."

    emocion_predominante = max(conteo, key=conteo.get)
    recomendaciones = {
        "feliz": "¡Sigue haciendo lo que te hace feliz! Considera compartir tu alegría con los demás.",
        "triste": "Parece que has estado sintiéndote triste últimamente. ¿Has pensado en hablar con alguien de confianza?",
        "enojado": "La ira puede acumularse con el tiempo. Intenta técnicas de relajación o actividades físicas.",
        "ansioso": "Si has estado ansioso con frecuencia, prueba ejercicios de respiración o meditación.",
        "neutral": "Tu estado emocional ha sido estable. Sigue cuidando tu bienestar emocional."
    }

def obtener_tendencias():
    # Código que devuelve las tendencias emocionales
    return {"tendencias": "Ejemplo de tendencia emocional"}

    return f"📊 Tendencia emocional detectada: {emocion_predominante}\n💡 Consejo: {recomendaciones[emocion_predominante]}"
