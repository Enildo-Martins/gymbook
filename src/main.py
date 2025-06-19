from models import Usuario

def tela_login():
    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    usuario = Usuario(username, senha)
    if usuario.autenticar():
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

if __name__ == "__main__":
    tela_login()
