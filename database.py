# dados/database.py
import sqlite3

DB_NAME = "livros.db"

def criar_tabela():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Tabela de livros (existente)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
            isbn TEXT PRIMARY KEY,
            titulo TEXT NOT NULL
        )
    """)
    
    # Nova tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def conectar():
    return sqlite3.connect(DB_NAME)