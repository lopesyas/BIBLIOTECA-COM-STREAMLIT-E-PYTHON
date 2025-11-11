# controller/usuario_controller.py
from model.usuario_model import Usuario
from service.usuario_service import criar_usuario, autenticar_usuario

def cadastrar_usuario(username, password, email):
    if not username or not password or not email:
        return False, "Preencha todos os campos!"
    
    if len(password) < 6:
        return False, "A senha deve ter pelo menos 6 caracteres!"
    
    usuario = Usuario(username, password, email)
    return criar_usuario(usuario)

def login_usuario(username, password):
    if not username or not password:
        return False, "Preencha todos os campos!"
    
    return autenticar_usuario(username, password)