class Aula:
    def __init__(self, id, capacidad, uso_especial=None):
        self.id = id
        self.capacidad = capacidad
        self.uso_especial = uso_especial

    def verificar_capacidad(self, estudiantes):
        return estudiantes <= self.capacidad
