# service/usuario_service.py
import sqlite3
import hashlib
from dados.database import conectar
from model.usuario_model import Usuario

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def criar_usuario(usuario):
    conn = conectar()
    cursor = conn.cursor()
    
    hashed_password = hash_password(usuario.password)
    
    try:
        cursor.execute("INSERT INTO usuarios (username, password, email) VALUES (?, ?, ?)",
                      (usuario.username, hashed_password, usuario.email))
        conn.commit()
        conn.close()
        return True, "Usuário criado com sucesso!"
    except sqlite3.IntegrityError as e:
        conn.close()
        if "username" in str(e):
            return False, "Nome de usuário já existe!"
        elif "email" in str(e):
            return False, "Email já cadastrado!"
        else:
            return False, f"Erro ao criar usuário: {e}"
    except Exception as e:
        conn.close()
        return False, f"Erro inesperado: {e}"

def autenticar_usuario(username, password):
    conn = conectar()
    cursor = conn.cursor()
    
    hashed_password = hash_password(password)
    
    cursor.execute("SELECT id, username, email FROM usuarios WHERE username = ? AND password = ?",
                  (username, hashed_password))
    usuario = cursor.fetchone()
    conn.close()
    
    if usuario:
        return True, Usuario(usuario[1], "", usuario[2], usuario[0])
    else:
        return False, "Usuário ou senha inválidos!"

def verificar_usuario_existe(username):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM usuarios WHERE username = ?", (username,))
    usuario = cursor.fetchone()
    conn.close()
    
    return usuario is not None