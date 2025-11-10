import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

# Cargar la clave del archivo .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(_name_)
MODEL = "models/gemini-2.5-flash"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(f"Responde de forma breve, práctica y con un máximo de 5 líneas. {prompt}")
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"⚠ Error: {e}"})

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))