import os

def carregar_prompt_base() -> str:
    caminho = os.path.join("src", "prompt.txt")
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return "⚠️ Prompt base não encontrado. Verifique se o arquivo 'prompt.txt' está em src/."
