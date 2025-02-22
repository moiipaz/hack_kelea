import json
import os
from datetime import datetime
from chatbot.emociones import analizar_emocion

DIARIO_PATH = "data/diario.json"

def guardar_entrada_diario(texto):
    """Guarda una entrada en el diario con la emoción detectada y almacena tendencias."""
    texto_limpio = texto.strip()
    if not texto_limpio:
        return {"error": "No se puede guardar una entrada vacía."}

    if not os.path.exists("data"):
        os.makedirs("data")

    try:
        with open(DIARIO_PATH, "r", encoding="utf-8") as file:
            diario = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        diario = []

    emocion = analizar_emocion(texto_limpio)

    entrada = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "texto": texto_limpio,
        "emocion": emocion
    }

    diario.append(entrada)

    with open(DIARIO_PATH, "w", encoding="utf-8") as file:
        json.dump(diario, file, indent=4, ensure_ascii=False)

    return {"mensaje": "Entrada guardada", "emocion": emocion}

def obtener_diario():
    """Obtiene todas las entradas del diario, asegurando que tengan fecha."""
    try:
        with open(DIARIO_PATH, "r", encoding="utf-8") as file:
            diario = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    for entry in diario:
        if "fecha" not in entry or not entry["fecha"]:
            entry["fecha"] = "2000-01-01 00:00:00"

    return sorted(diario, key=lambda x: datetime.strptime(x["fecha"], "%Y-%m-%d %H:%M:%S"), reverse=True)

def obtener_tendencias():
    """Analiza las emociones almacenadas y genera una tendencia emocional."""
    diario = obtener_diario()
    if not diario:
        return "No hay suficientes datos para detectar tendencias."

    conteo = {}
    for entry in diario:
        emocion = entry["emocion"]
        conteo[emocion] = conteo.get(emocion, 0) + 1

    if not conteo:
        return "No hay datos suficientes."

    emocion_predominante = max(conteo, key=conteo.get)
    return f"📊 Emoción predominante: {emocion_predominante} ({conteo[emocion_predominante]} veces)"
