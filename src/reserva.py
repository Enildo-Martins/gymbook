class Reserva:
    horarios_reservados = set()

    def __init__(self, horario):
        self.horario = horario

    def reservar(self):
        if self.horario in Reserva.horarios_reservados:
            return False
        Reserva.horarios_reservados.add(self.horario)
        return True
