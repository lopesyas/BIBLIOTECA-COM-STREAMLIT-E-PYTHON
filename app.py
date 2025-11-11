# app.py
import streamlit as st
from controller.livro_controller import cadastrar_livro, obter_livros
from dados.database import criar_tabela
from login.usuario import mostrar_login, mostrar_usuario_logado

# Configuração da página
st.set_page_config(
    page_title="Sistema de Biblioteca",
    page_icon="📚",
    layout="wide"
)

# Cria tabelas na inicialização
criar_tabela()

st.title("📚 Sistema de Biblioteca")

# Sistema de login
usuario_autenticado = mostrar_login()

if usuario_autenticado:
    # Mostrar informações do usuário logado
    mostrar_usuario_logado()
    
    # Conteúdo principal (apenas para usuários logados)
    st.markdown("---")
    st.header("Cadastro de Livros")

    # Formulário de livros
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("➕ Adicionar novo livro")
        with st.form("form_livro", clear_on_submit=True):
            isbn = st.text_input("ISBN")
            titulo = st.text_input("Título")
            submitted = st.form_submit_button("Cadastrar Livro")

            if submitted:
                if isbn and titulo:
                    mensagem = cadastrar_livro(isbn, titulo)
                    st.success(mensagem)
                else:
                    st.error("Preencha ISBN e Título!")

    with col2:
        st.subheader("📖 Livros cadastrados")
        livros = obter_livros()

        if livros:
            for livro in livros:
                st.write(f"**ISBN:** {livro[0]} | **Título:** {livro[1]}")
        else:
            st.info("Nenhum livro cadastrado ainda.")
else:
    # Mensagem quando usuário não está logado
    st.markdown("---")
    st.info("🔐 Faça login ou cadastre-se para acessar o sistema de livros.")

# Debug: Mostrar estado da sessão (opcional - pode remover depois)
with st.sidebar:
    st.markdown("---")
    if st.checkbox("🔧 Debug Session State"):
        st.write("Estado da sessão:", dict(st.session_state))

# No início do app.py, após as importações
if st.sidebar.button("🔄 Reset Login"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()