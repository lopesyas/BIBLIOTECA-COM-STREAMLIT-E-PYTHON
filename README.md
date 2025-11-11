# BIBLIOTECA-COM-STREAMLIT-E-PYTHON
Um sistema completo de gerenciamento de biblioteca desenvolvido em Python com Streamlit, incluindo autenticação de usuários e cadastro de livros.


-- Funcionalidades

Sistema de Autenticação
Cadastro de usuários com validação de dados
Login seguro com hash de senhas
Controle de sessão com Streamlit Session State
Logout com um clique
Gerenciamento de Livros
Cadastro de livros com ISBN e título
Listagem de todos os livros cadastrados
Interface intuitiva e responsiva
Validação de campos obrigatórios

-- Tecnologias Utilizadas
Python 3.x
Streamlit - Framework para aplicações web
SQLite - Banco de dados relacional
SHA-256 - Criptografia de senhas

-- Estrutura do Projeto

BIBLIOTECA/
├── controller/
│ ├── livro_controller.py
│ └── usuario_controller.py
├── model/
│ ├── livro_model.py
│ └── usuario_model.py
├── service/
│ ├── livro_service.py
│ └── usuario_service.py
├── dados/
│ └── database.py
├── login/
│ └── usuario.py
├── app.py
└── README.md

-- Instalação e Configuração
Pré-requisitos: 

Python 3.8 ou superior
pip (gerenciador de pacotes do Python)

-- Passos para instalação

Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

Instale as dependências
pip install streamlit

Execute a aplicação
streamlit run app.py

Acesse no navegador
http://localhost:8501

-- Como Usar
Primeiro Acesso
Ao abrir a aplicação, você verá a tela de login
Clique em "Não tem conta? Cadastre-se aqui"
Preencha os dados: usuário, email e senha (mínimo 6 caracteres)
Clique em "Criar Conta"
Após o Login
Cadastrar Livros:
Preencha ISBN e Título
Clique em "Cadastrar Livro"
Visualizar Livros:
Todos os livros cadastrados aparecem na lista à direita

Logout:

Clique em "Sair do Sistema" no sidebar

-- Segurança:

Senhas criptografadas usando SHA-256
Validação de dados em todos os formulários
Controle de sessão para proteger rotas
Tratamento de erros para evitar vazamento de informações

-- Banco de Dados
O sistema utiliza SQLite com duas tabelas principais:

Tabela: usuarios
CREATE TABLE usuarios(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL,
email TEXT UNIQUE NOT NULL
)

Tabela: livros
CREATE TABLE livros(
isbn TEXT PRIMARY KEY,
titulo TEXT NOT NULL
)

-- Desenvolvimento
Adicionando Novas Funcionalidades
Novos Models: Adicione em model/
Novos Services: Adicione em service/
Novos Controllers: Adicione em controller/
Novas Interfaces: Adicione em login/ ou modifique app.py

-- Estrutura MVC
O projeto segue o padrão MVC (Model-View-Controller):
Model: Define a estrutura dos dados
View: Interface do usuário (Streamlit)
Controller: Lógica de negócio e comunicação entre Model e View

-- Solução de Problemas
Erro Comuns
"Port already in use"
streamlit run app.py --server.port 8502
Problemas com banco de dados
Delete o arquivo livros.db para recriar as tabelas
rm livros.db

-Problemas de importação
Verifique se todos os arquivos estão nas pastas corretas
Confirme que o Python path está configurado corretamente

-- Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para:
Reportar bugs
Sugerir novas funcionalidades
Enviar pull requests

-- Suporte
Se você encontrar algum problema ou tiver dúvidas:
Verifique a seção de Solução de Problemas acima
Abra uma issue no repositório

Entre em contato com o desenvolvedor

Desenvolvido com Python e Streamlit
