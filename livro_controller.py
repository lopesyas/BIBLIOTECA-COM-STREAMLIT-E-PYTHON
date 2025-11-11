from model.livro_model import Livro
from service.livro_service import salvar_livro, listar_livros

def cadastrar_livro(isbn, titulo):
    if not isbn or not titulo:
        return "Preencha todos os campos!"
    livro = Livro(isbn, titulo)
    try:
        salvar_livro(livro)
        return f"Livro '{titulo}' cadastrado com sucesso!"
    except Exception as e:
        return f"Erro ao cadastrar: {e}"

def obter_livros():
    return listar_livros()
