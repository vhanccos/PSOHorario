class Particula:
    def __init__(self, solucion):
        self.solucion = (
            solucion  # Matriz tridimensional representando la asignación de horarios
        )
        self.fitness = None

    def calcular_fitness(self):
        # TODO: Implementar lógica para calcular el fitness
        self.fitness = 100  # Ejemplo estático, implementar la lógica adecuada
        return self.fitness

    @staticmethod
    def generar_particula_inicial():
        # TODO: Implementar lógica para generar una solución inicial válida
        return Particula(solucion=[])
