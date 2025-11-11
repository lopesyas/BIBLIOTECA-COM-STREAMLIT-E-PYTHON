# model/usuario_model.py
class Usuario:
    def __init__(self, username: str, password: str, email: str, id=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email