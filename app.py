import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Carrega .env
load_dotenv()

# Configura Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-3-flash-preview")



# -------------------------
# Classificação da pergunta
# -------------------------
def classificar_pergunta(pergunta):
    prompt = f"""
Classifique a pergunta em apenas UMA dessas categorias:
camisa, caneca, banner, geral

Pergunta: "{pergunta}"
Responda somente com a categoria.
"""
    resposta = model.generate_content(prompt)
    return resposta.text.strip().lower()

# -------------------------
# Escolha do arquivo
# -------------------------
def escolher_arquivo_por_categoria(categoria):
    return {
        "camisa": "dados/camisa.txt",
        "caneca": "dados/caneca.txt",
        "banner": "dados/banner.txt",
        "geral": "dados/geral.txt"
    }.get(categoria, "dados/geral.txt")

# -------------------------
# Interface Streamlit
# -------------------------
st.title("🤖 Chatbot da Gráfica")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    try:
        categoria = classificar_pergunta(pergunta)
        arquivo = escolher_arquivo_por_categoria(categoria)

        with open(arquivo, "r", encoding="utf-8") as f:
            contexto = f.read()

        prompt_final = f"""
Você é um atendente de uma gráfica.
Use APENAS as informações abaixo para responder.
Se não souber, diga que não possui essa informação.

INFORMAÇÕES:
{contexto}

PERGUNTA:
{pergunta}
"""

        resposta = model.generate_content(prompt_final)
        resposta_final = resposta.text

    except Exception as e:
        erro = str(e).lower()

        if "quota" in erro or "limit" in erro or "token" in erro or "429" in erro:
            resposta_final = (
                "⚠️ Serviço temporariamente indisponível.\n\n"
                "O limite de uso da inteligência artificial foi atingido.\n"
                "Por favor, tente novamente mais tarde."
            )
        else:
            resposta_final = (
                "❌ Ocorreu um erro ao processar sua pergunta.\n\n"
                "Tente novamente ou reformule a pergunta."
            )

    st.write(resposta_final)