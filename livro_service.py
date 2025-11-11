from dados.database import conectar

def salvar_livro(livro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (isbn, titulo) VALUES (?, ?)",
                  (livro.isbn, livro.titulo))
    conn.commit()
    conn.close()

def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT isbn, titulo FROM livros')  
    livros = cursor.fetchall()
    conn.close()
    return livros
