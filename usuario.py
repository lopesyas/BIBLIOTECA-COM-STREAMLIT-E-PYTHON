# login/usuario.py
import streamlit as st
from controller.usuario_controller import cadastrar_usuario, login_usuario

def mostrar_form_login():
    st.markdown("---")
    st.subheader("🔐 Login")
    
    with st.form("form_login"):
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")
        
        if submitted:
            if username and password:
                sucesso, resultado = login_usuario(username, password)
                if sucesso:
                    st.session_state["usuario_logado"] = {
                        "id": resultado.id,
                        "username": resultado.username,
                        "email": resultado.email
                    }
                    st.success(f"Bem-vindo, {resultado.username}!")
                    st.rerun()
                else:
                    st.error(resultado)
            else:
                st.error("Preencha todos os campos!")
    
    # Link para cadastro
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("📝 Cadastrar"):
            st.session_state["mostrar_cadastro"] = True
            st.rerun()

def mostrar_form_cadastro():
    st.markdown("---")
    st.subheader("📝 Cadastro de Usuário")
    
    with st.form("form_cadastro"):
        username = st.text_input("Usuário")
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")
        confirm_password = st.text_input("Confirmar Senha", type="password")
        submitted = st.form_submit_button("Cadastrar")
        
        if submitted:
            if not username or not email or not password:
                st.error("Preencha todos os campos!")
            elif password != confirm_password:
                st.error("As senhas não coincidem!")
            else:
                sucesso, mensagem = cadastrar_usuario(username, password, email)
                if sucesso:
                    st.success(mensagem)
                    st.session_state["mostrar_cadastro"] = False
                    st.rerun()
                else:
                    st.error(mensagem)
    
    # Link para login
    if st.button("↩️ Voltar para Login"):
        st.session_state["mostrar_cadastro"] = False
        st.rerun()

def mostrar_login():
    # Inicializar estado da sessão se não existir
    if "usuario_logado" not in st.session_state:
        st.session_state["usuario_logado"] = None
    if "mostrar_cadastro" not in st.session_state:
        st.session_state["mostrar_cadastro"] = False
    
    # Container para o login/cadastro
    with st.container():
        # Se usuário não está logado, mostrar formulários
        if not st.session_state["usuario_logado"]:
            if st.session_state["mostrar_cadastro"]:
                mostrar_form_cadastro()
            else:
                mostrar_form_login()
            return False
        else:
            # Usuário está logado
            return True

def logout():
    if st.sidebar.button("🚪 Sair"):
        st.session_state["usuario_logado"] = None
        st.session_state["mostrar_cadastro"] = False
        st.success("Logout realizado com sucesso!")
        st.rerun()

def mostrar_usuario_logado():
    if st.session_state["usuario_logado"]:
        st.sidebar.markdown("---")
        st.sidebar.success(f"👋 Olá, **{st.session_state['usuario_logado']['username']}**!")
        st.sidebar.info(f"📧 {st.session_state['usuario_logado']['email']}")
        logout()