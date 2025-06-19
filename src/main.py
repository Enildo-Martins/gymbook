from models import Usuario
from reserva import Reserva

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

def tela_reserva():
    horario = input("Digite o horário para reservar (ex: 18:00): ")
    reserva = Reserva(horario)
    if reserva.reservar():
        print(f"Reserva realizada com sucesso para às {horario}!")
    else:
        print(f"Horário das {horario} já reservado!")

if __name__ == "__main__":
    tela_reserva()
