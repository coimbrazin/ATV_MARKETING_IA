import streamlit as st
import html
import base64
from marketing_brain import responder_pergunta

st.set_page_config(page_title="IA de Marketing EMS", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #003366, #00ADEF);
        color: #FFFFFF;
        min-height: 100vh;
        padding: 0;
        margin: 0;
    }
    header, .css-1v3fvcr, .css-1r6slb0, .css-10trblm {
        display: none !important;
    }
    div[data-testid="stMarkdownContainer"] div p {
        color: #ffffff !important;
    }
    .css-18e3th9 {
        color: white !important;
        margin-top: 0;
        padding-top: 0;
    }

     /* Estilo para a imagem do cabeçalho */
    .nickia-header-img {
        border-radius: 15px;  /* Bordas menos arredondadas */
        width: 250px;
        height: auto;
        object-fit: cover;
    }
    
    /* Estilo para a imagem das mensagens (já existente) */
    .nickia-msg-img {
        border-radius: 50%;  /* Formato circular */
        width: 70px;
        height: 70px;
        object-fit: cover;
        vertical-align: middle;
        margin-right: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Função para converter imagem em base64
def img_to_base64_str(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# Imagens base64 - AGORA COM DUAS IMAGENS DIFERENTES
nickia_header_img_base64 = img_to_base64_str("src/assets/nickia_foto-semfundo.png")  # Imagem para o cabeçalho
nickia_chat_img_base64 = img_to_base64_str("src/assets/nickia_conversa.png")     # Imagem para o chat
ems_logo_base64 = img_to_base64_str("src/assets/ems_logo.png")

# HTML para a imagem do chat
nickia_img_html = f'<img src="data:image/png;base64,{nickia_chat_img_base64}" class="nickia-msg-img">'

# Cabeçalho
st.markdown(
    f"""
    <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; gap: 50px;">
            <img src="data:image/png;base64,{nickia_header_img_base64}" width="250" style="margin: 0;">
            <h1 style="margin: 0; padding: 0; line-height: 1;">NickIA - IA Especialista em Marketing EMS</h1>
        </div>
        <div style="display: flex; align-items: center;">
            <img src="data:image/png;base64,{ems_logo_base64}" width="150" style="margin: 20;">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Inicializa histórico
if "historico" not in st.session_state:
    st.session_state.historico = []

# Mensagem automática ao iniciar
if "mensagem_inicial_enviada" not in st.session_state:
    st.session_state.historico.append({
        "autor": "ia",
        "mensagem": "👋 Olá! Eu sou a Nick, a inteligência artificial de marketing da EMS! "
                    "Me diga, como posso te ajudar hoje?"
    })
    st.session_state.mensagem_inicial_enviada = True

# Entrada de pergunta
pergunta = st.chat_input("Digite sua dúvida de marketing...")

if pergunta:
    st.session_state.historico.append({"autor": "usuário", "mensagem": pergunta})
    resposta = responder_pergunta(pergunta)
    st.session_state.historico.append({"autor": "ia", "mensagem": resposta})

# Exibe histórico
for item in st.session_state.historico:
    if item["autor"] == "usuário":
        col1, col2, col3 = st.columns([1, 0.2, 3])
        with col3:
            st.markdown(
                f"""
                <div style='
                    text-align: right;
                    background: linear-gradient(135deg, #00ADEF, #0099CC);
                    color: white;
                    padding: 12px;
                    border-radius: 15px;
                    margin-bottom: 8px;
                    font-weight: 600;
                '>
                    🙋 {html.escape(item["mensagem"])}
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        col1, col2, col3 = st.columns([0.40, 0.1, 6])
        with col1:
            st.markdown(nickia_img_html, unsafe_allow_html=True)
        with col3:
            st.markdown(
                f"""
                <div style='
                    text-align: left;
                    background: linear-gradient(135deg, #003366, #005599);
                    color: white !important;
                    padding: 12px;
                    border-radius: 15px;
                    margin-bottom: 8px;
                    font-weight: 600;
                '>
                     {html.escape(item["mensagem"])}
                </div>
                """,
                unsafe_allow_html=True,
            )

# Exportar histórico como .txt
def exportar_historico_txt(historico):
    texto = ""
    for item in historico:
        autor = "Você" if item["autor"] == "usuário" else "NickIA"
        texto += f"{autor}: {item['mensagem']}\n\n"
    return texto

st.divider()
st.markdown("### 📄 Exportar Conversa")
if st.button("Salvar histórico como .txt"):
    conteudo = exportar_historico_txt(st.session_state.historico)
    b64 = base64.b64encode(conteudo.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="chat_nickia.txt">📥 Clique aqui para baixar</a>'
    st.markdown(href, unsafe_allow_html=True)
