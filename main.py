import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate



st.set_page_config(
    page_title="ChatBot Gaúcho",
    layout="centered"
)

# Criar o meu Titulo
st.title("Meu ChatBot é Gaúcho")

#Criando o sidebar
with st.sidebar:

    st.markdown("##  Configurações")
    st.markdown("---")

    groq_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="API_...",
        help="Crie sua chave em console.groq.com/keys"
    )

# Gera a separação entre as interfaces

    st.markdown("---")

    contexto = st.text_area(
            "Contexto do Assistente",
            value="Você é um assistente virtual com personalidade de um gaúcho raiz do interior do Rio Grande do Sul, fala de forma informal com sotaque leve usando expressões como “Bah”, “Tchê”, “Meo”, “Tri” e “Capaz” sem exagero, mantém energia positiva influenciada por futebol e cultura reggae, trata o usuário como “vivente” ou “parceiro”, é sempre prestativo e claro mesmo em assuntos sérios, adapta o tom conforme o contexto e nunca perde a essência simples, autêntica e acolhedora do pampa.",
            height=150
        )

	# Escolha de modelos
modelo = st.selectbox(
		"Modelo Groq",
		[
			"llama-3.3-70b-versatile",
			"llama3-8b-8192",
			"mixtral-8x7b-32768"
		]
	)

# Ajuste de Temperatura
temperatura = st.slider(
	"Temperatura (criatividade)",
	0.0, 1.0, 0.3
)

# Limpar a memoria
st.markdown("---")

if st.button(" Limpar conversa"):
	st.session_state.mensagens = []
	st.rerun()

# Desenvolvedor(a)
st.markdown("---")
st.markdown(
	"<small>Maria Eduarda <3</small>",
	unsafe_allow_html=True
)	

# FUNÇÃO DO BOT
def resposta_bot(mensagens):

    chat = ChatGroq(
        model=modelo,
        api_key=groq_key,
        temperature=temperatura
    )

    mensagens_modelo = [("system", contexto)]
    mensagens_modelo += mensagens

    prompt = ChatPromptTemplate.from_messages(mensagens_modelo)

    chain = prompt | chat

    resposta = chain.invoke({})

    return resposta.content


# MEMÓRIA DO CHAT

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        ("assistant", "Fala aí, vivente...")
    ]


# MOSTRAR HISTÓRICO

for role, content in st.session_state.mensagens:

    with st.chat_message(role):
        st.markdown(content)


# INPUT DO USUÁRIO
pergunta = st.chat_input("Digite sua pergunta...")


if pergunta:

    if not groq_key:
        st.warning(" Informe sua Groq API Key no menu lateral.")
        st.stop()

    st.session_state.mensagens.append(("user", pergunta))

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):

            resposta = resposta_bot(st.session_state.mensagens)

            st.markdown(resposta)

    st.session_state.mensagens.append(("assistant", resposta))
