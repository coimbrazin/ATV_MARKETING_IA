import streamlit as st
import html
from marketing_brain import responder_pergunta

st.set_page_config(page_title="NickIA - IA de Marketing EMS", layout="wide")

st.markdown(
    """
    <style>
    /* Fundo gradient EMS */
    .stApp {
        background: linear-gradient(135deg, #003366, #00ADEF);
        color: #FFFFFF;
        min-height: 100vh;
        padding: 0;
        margin: 0;
    }

    /* Remove barra superior (header) */
    header,
    .css-1v3fvcr,
    .css-1r6slb0,
    .css-10trblm {
        display: none !important;
    }

    /* Ajusta containers de markdown para texto preto nas bolhas claras */
    div[data-testid="stMarkdownContainer"] div p {
        color: #ffffff !important;
    }

    /* Títulos em branco para contraste */
    .css-18e3th9 {
        color: white !important;
        margin-top: 0;
        padding-top: 0;
    }

    /* Força texto branco nas respostas da IA */
    .resposta-ia * {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Exibe a logo EMS no topo
st.image("src/assets/ems_logo.png", width=150)

if "historico" not in st.session_state:
    st.session_state.historico = []

st.title("💡 NickIA - IA Especialista em Marketing EMS")

pergunta = st.chat_input("Digite sua dúvida de marketing...")

if pergunta:
    st.session_state.historico.append({"autor": "usuário", "mensagem": pergunta})
    resposta = responder_pergunta(pergunta)
    st.session_state.historico.append({"autor": "nickia", "mensagem": resposta})

for item in st.session_state.historico:
    if item["autor"] == "usuário":
        col1, col2, col3 = st.columns([1, 0.2, 3])
        with col3:
            st.markdown(f"""
                <div style='
                    text-align: right;
                    background: linear-gradient(135deg, #00ADEF, #0099CC);
                    color: white !important;
                    padding: 12px;
                    border-radius: 15px;
                    margin-bottom: 8px;
                    font-weight: 600;
                '>
                    🙋 {html.escape(item["mensagem"])}
                </div>
            """, unsafe_allow_html=True)
    else:
        col1, col2, col3 = st.columns([3, 0.2, 1])
        with col1:
            # Aplicando classe resposta-ia para forçar cor branca via CSS
            st.markdown(f"""
                <div class='resposta-ia' style='
                    text-align: left;
                    background: linear-gradient(135deg, #003366, #005599);
                    padding: 12px;
                    border-radius: 15px;
                    margin-bottom: 8px;
                    font-weight: 600;
                '>
                    🤖 NickIA: {html.escape(item["mensagem"])}
                </div>
            """, unsafe_allow_html=True)
