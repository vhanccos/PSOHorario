class Turno:
    def __init__(self, id, nombre, horario_disponible):
        self.id = id
        self.nombre = nombre
        self.horario_disponible = (
            horario_disponible  # Ejemplo: {"inicio": "7:00", "fin": "13:00"}
        )

    def validar_horario(self, inicio, fin):
        return (
            self.horario_disponible["inicio"] <= inicio
            and fin <= self.horario_disponible["fin"]
        )
