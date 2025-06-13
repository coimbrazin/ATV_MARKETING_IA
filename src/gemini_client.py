import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Carrega a chave da API do .env
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# Cria o modelo Gemini 2.0 Flash
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def gerar_resposta_gemini(mensagem: str) -> str:
    try:
        response = model.generate_content(mensagem)
        return response.text
    except Exception as e:
        return f"❌ Erro ao gerar resposta: {str(e)}"
