function sendMessage() {
    let userInput = document.getElementById("userInput").value;

    fetch("/diario", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = `Emoción detectada: ${data.emocion}`;
    })
    .catch(error => console.error("Error:", error));
}

function enviarTestPersonalidad() {
    // Capturar los valores de los inputs de tipo número
    let respuestas = [
        parseInt(document.getElementById("apertura").value) || 0,
        parseInt(document.getElementById("responsabilidad").value) || 0,
        parseInt(document.getElementById("extraversión").value) || 0,
        parseInt(document.getElementById("amabilidad").value) || 0,
        parseInt(document.getElementById("neuroticismo").value) || 0
    ];

    // Capturar los valores del eneagrama
    let eneagramaRespuestas = [
        document.getElementById("problemas").value.trim(),
        document.getElementById("motivación").value.trim(),
        document.getElementById("estrés").value.trim()
    ];

    // Combinar todas las respuestas en un solo array
    let todasLasRespuestas = respuestas.concat(eneagramaRespuestas);

    // Verificar que todas las respuestas están completas
    if (todasLasRespuestas.some(r => r === "" || r === null || r === undefined)) {
        alert("⚠️ Debes responder todas las preguntas antes de enviar.");
        return;
    }

    console.log("Enviando respuestas:", todasLasRespuestas); // Verificar en la consola

    fetch("/test_personalidad", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ respuestas: todasLasRespuestas })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("⚠️ " + data.error);
        } else {
            document.getElementById("resultadoTest").innerHTML = 
                `<strong>🧠 Resultado del Test:</strong> ${data.tipo}`;
        }
    })
    .catch(error => console.error("Error:", error));
}

function enviarTest() {
    let respuestas = [
        parseInt(document.getElementById("q1").value),
        parseInt(document.getElementById("q2").value),
        parseInt(document.getElementById("q3").value),
        parseInt(document.getElementById("q4").value),
        parseInt(document.getElementById("q5").value),
        document.getElementById("q6").value,
        document.getElementById("q7").value,
        document.getElementById("q8").value
    ];

    fetch("/test_personalidad", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ respuestas })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("⚠️ " + data.error);
        } else {
            let resultado = `
                <strong>Big Five:</strong><br>
                Apertura: ${data["Big Five"]["Apertura"]}<br>
                Responsabilidad: ${data["Big Five"]["Responsabilidad"]}<br>
                Extraversión: ${data["Big Five"]["Extraversión"]}<br>
                Amabilidad: ${data["Big Five"]["Amabilidad"]}<br>
                Neuroticismo: ${data["Big Five"]["Neuroticismo"]}<br><br>
                
                <strong>Eneagrama:</strong> ${data["Eneagrama"]}
            `;
            document.getElementById("resultadoTest").innerHTML = resultado;
        }
    })
    .catch(error => console.error("Error:", error));
}
