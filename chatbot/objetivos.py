def generar_objetivos(emocion):
    """Genera objetivos de bienestar según la emoción detectada."""
    recomendaciones = {
        "feliz": [
            "Mantén tu rutina y sigue disfrutando de las cosas que te hacen sentir bien.",
            "Comparte tu felicidad con otros para fortalecer relaciones positivas."
        ],
        "triste": [
            "Habla con alguien de confianza sobre cómo te sientes.",
            "Haz algo que normalmente disfrutes, como escuchar música o salir a caminar."
        ],
        "ansioso": [
            "Practica la respiración profunda o meditación para calmar tu mente.",
            "Organiza tu día en pequeñas tareas para reducir el estrés."
        ],
        "enfadado": [
            "Tómate un momento para respirar y reflexionar antes de actuar.",
            "Realiza actividad física para canalizar la energía de manera positiva."
        ],
        "tranquilo": [
            "Explora nuevas actividades o hobbies para enriquecer tu día.",
            "Reflexiona sobre lo que te gustaría mejorar o cambiar en tu vida."
        ]
    }

    return recomendaciones.get(emocion, ["No sé cómo ayudarte con esa emoción en este momento."])
