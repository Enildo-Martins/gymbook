from models import Usuario, Reserva

def simular_reserva(usuario_nome, horario):
    usuario = Usuario(usuario_nome)
    reserva = Reserva(usuario, horario)
    print(f"Reserva feita por {usuario.nome} para o horário {reserva.horario}")

if __name__ == "__main__":
    simular_reserva("João", "18:00")
