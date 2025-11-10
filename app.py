from flask import Flask, request, jsonify
import google.generativeai as genai
import os

# Configura tu API Key desde el entorno
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "")

    # Configurar el modelo
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generar respuesta
    response = model.generate_content(
        f"Responde de manera amable, clara y breve (máximo 80 palabras) a la siguiente pregunta: {user_message}"
    )

    return jsonify({"response": response.text.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)