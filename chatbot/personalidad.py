def evaluar_personalidad(respuestas):
    """
    Evalúa la personalidad del usuario en base a sus respuestas al test.
    Se espera que respuestas sea una lista de 8 valores (5 para Big Five, 3 para Eneagrama).
    """
    if len(respuestas) != 8:
        return {"error": "Se requieren 8 respuestas para evaluar la personalidad."}

    # Big Five: Respuestas de 1 a 5
    big_five = {
        "Apertura": respuestas[0],
        "Responsabilidad": respuestas[1],
        "Extraversión": respuestas[2],
        "Amabilidad": respuestas[3],
        "Neuroticismo": respuestas[4]
    }

    # Eneagrama: Respuestas de selección (a, b, c)
    eneagrama_map = {
        "6a": "Controlador", "6b": "Emocional", "6c": "Evasivo",
        "7a": "Competitivo", "7b": "Social", "7c": "Pacifista",
        "8a": "Dominante", "8b": "Reservado", "8c": "Dependiente"
    }
    
    tipo_eneagrama = eneagrama_map.get(f"6{respuestas[5]}", "Desconocido") + " / " + \
                     eneagrama_map.get(f"7{respuestas[6]}", "Desconocido") + " / " + \
                     eneagrama_map.get(f"8{respuestas[7]}", "Desconocido")

    return {
        "Big Five": big_five,
        "Eneagrama": tipo_eneagrama
    }
