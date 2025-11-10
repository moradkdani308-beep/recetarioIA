import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

# Cargar la clave del archivo .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)
MODEL = "models/gemini-2.5-flash"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip().lower()
    try:
        # Detectar saludos o agradecimientos
        if any(word in user_input for word in ["gracias", "thank", "hola", "buenas", "adiós"]):
            return jsonify({"response": "¡De nada! 😊 Si quieres otra receta o consejo, dime qué te gustaría preparar."})
        
        # Generar receta o explicación paso a paso con subsecciones
        model = genai.GenerativeModel(MODEL)
        prompt = (
            "Eres un chef tutor que explica recetas de cocina paso a paso para principiantes. "
            "Si la receta es compleja, divide la respuesta en subsecciones: "
            "**Ingredientes**, **Preparación**, **Consejos/Tips**. "
            "Cada paso o consejo debe estar en una línea separada. "
            "Máximo 120 palabras. Explica todo de manera clara y ordenada: "
            f"{user_input}"
        )
        response = model.generate_content(prompt)
        
        return jsonify({"response": response.text})
    
    except Exception as e:
        return jsonify({"response": f"⚠ Error: {e}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))