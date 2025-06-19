class Usuario:
    def __init__(self, nome):
        self.nome = nome

class Reserva:
    def __init__(self, usuario, horario):
        self.usuario = usuario
        self.horario = horario
