from flask import Flask, render_template, request, jsonify
import os
import json
from chatbot.emociones import analizar_emocion, responder_emocion, obtener_tendencias
from chatbot.diario import guardar_entrada_diario, obtener_diario, obtener_tendencias
from chatbot.personalidad import evaluar_personalidad
from chatbot.objetivos import generar_objetivos
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """Recibe un mensaje del usuario y devuelve la emoción detectada con una respuesta."""
    data = request.json
    texto = data.get("texto", "").strip()
    if not texto:
        return jsonify({"error": "El mensaje no puede estar vacío"}), 400

    emocion = analizar_emocion(texto)
    respuesta = responder_emocion(emocion)

    return jsonify({"emocion": emocion, "respuesta": respuesta})

@app.route('/chatbot/tendencias', methods=['GET'])
def tendencias_emocionales():
    """Devuelve tendencias emocionales analizadas a partir del historial."""
    return jsonify({"tendencias": obtener_tendencias_emocionales()})



def cargar_diario():
    """Carga las entradas del diario desde un archivo JSON."""
    if not os.path.exists("data/diario.json"):
        return []
    
    with open("data/diario.json", "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []  
@app.route('/diario', methods=['GET', 'POST'])
def manejar_diario():
    if request.method == 'POST':
        data = request.json
        texto = data.get("texto", "").strip()
        if not texto:
            return jsonify({"error": "El texto no puede estar vacío"}), 400
        return jsonify(guardar_entrada_diario(texto))
    
    entradas = cargar_diario()
    return render_template("diario.html", entradas=entradas)

@app.route('/diario/tendencias', methods=['GET'])
def obtener_tendencias_api():
    """Devuelve las tendencias emocionales detectadas."""
    return jsonify({"tendencia": obtener_tendencias()})



@app.route('/test_personalidad', methods=['GET', 'POST'])
def test_personalidad():
    if request.method == "GET":
        return render_template("personalidad.html")  
    
    data = request.json
    respuestas = data.get("respuestas", [])

    if not respuestas or len(respuestas) != 8:
        return jsonify({"error": "Se requieren 8 respuestas válidas"}), 400

    resultado = evaluar_personalidad(respuestas)  
    return jsonify(resultado)




@app.route('/objetivos', methods=['POST'])
def obtener_objetivos():
    data = request.json
    tipo_personalidad = data.get("tipo_personalidad", "").strip()
    if not tipo_personalidad:
        return jsonify({"error": "Falta el tipo de personalidad"}), 400
    objetivos = generar_objetivos(tipo_personalidad)
    return jsonify({"objetivos": objetivos})

@app.route('/coach', methods=['POST'])
def coach():
    """Recibe el estado emocional del usuario y devuelve objetivos personalizados."""
    data = request.json
    emocion = data.get("emocion", "").strip()

    if not emocion:
        return jsonify({"error": "Debe indicar una emoción"}), 400

    objetivos = generar_objetivos(emocion)
    return jsonify({"emocion": emocion, "objetivos": objetivos})

@app.route('/coach', methods=['GET'])
def mostrar_coach():
    return render_template("coach.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
