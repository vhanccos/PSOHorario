class Docente:
    def __init__(self, id, nombre, tipo, disponibilidad, horas_max, horas_min):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo  # Ejemplo: SubProfesorA, SubProfesorB
        self.disponibilidad = disponibilidad  # Horas disponibles
        self.horas_max = horas_max
        self.horas_min = horas_min

    def verificar_disponibilidad(self, horario):
        return horario in self.disponibilidad
