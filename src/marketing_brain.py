from gemini_client import gerar_resposta_gemini
from utils import carregar_prompt_base
import re

def responder_pergunta(pergunta_usuario: str) -> str:
    prompt_base = carregar_prompt_base()

    # Monta a entrada final combinando o prompt base + pergunta do usuário
    entrada_formatada = f"{prompt_base.strip()}\n\n/// PERGUNTA DO USUÁRIO:\n{pergunta_usuario.strip()}"

    # Chama a IA Gemini
    resposta = gerar_resposta_gemini(entrada_formatada)

    # Remove tags <div> e </div> da resposta, se houver
    resposta_limpa = re.sub(r'</?div>', '', resposta).strip()

    return resposta_limpa
