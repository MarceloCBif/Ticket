class User:
    def __init__(self, usuario, senha, email):
        self.usuario = usuario
        self.senha = senha
        self.email = email
    
    def __str__(self):
        return f"Usuário: {self.username}\nEmail: {self.email}\n"

