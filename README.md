# GroqStream Chatbot

Um assistente virtual moderno que combina a simplicidade do **Streamlit** com a velocidade absurda de inferência da **Groq API**.

## Sobre o Projeto
Este projeto foi desenvolvido para demonstrar como criar uma interface de chat robusta e responsiva utilizando modelos de linguagem de última geração (LLMs) via Groq. O diferencial aqui é a **latência quase zero**, proporcionando uma experiência de conversação muito mais natural.

### Tecnologias Utilizadas
* **Python 3.x**: Linguagem base.
* [**Streamlit**](https://streamlit.io/): Para a interface web interativa.
* [**Groq Cloud API**](https://groq.com/): Para processamento de linguagem natural ultra-rápido.
* **Python-dotenv**: Para gerenciamento de variáveis de ambiente de forma segura.

## Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/dudinha-web/chatbot.git](https://github.com/dudinha-web/chatbot.git)
   cd chatbot
   
2. **Crie um ambiente virtual:**

Bash
python -m venv venv
No Windows: venv\Scripts\activate

3. **Instale as dependências:**
Bash
pip install -r requirements.txt

4. **Configure suas chaves:**
Crie um arquivo .env na raiz do projeto e adicione sua API KEY:
Snippet de código
GROQ_API_KEY=sua_chave_aqui

5. **Execute a aplicação:**

Bash
streamlit run main.py

### Funcionalidades

Velocidade: Respostas em milissegundos graças à LPU (Language Processing Unit) da Groq.

Interface Clean: Design focado na experiência do usuário.

Histórico de Chat: Mantém o contexto da conversa durante a sessão.

Configuração Customizável: Fácil de trocar o modelo.

### Segurança

O projeto utiliza variáveis de ambiente para garantir que chaves de API sensíveis não sejam expostas no histórico do Git. Certifique-se de adicionar o .env ao seu .gitignore.

Desenvolvido por Dudinha <3
