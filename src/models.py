class Usuario:
    usuarios = {"user1": "1234", "user2": "abcd"}

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def autenticar(self):
        return Usuario.usuarios.get(self.nome) == self.senha
