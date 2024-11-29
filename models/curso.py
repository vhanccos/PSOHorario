class Curso:
    def __init__(self, id, nombre, horas_semanales, docentes_calificados, ciclo):
        self.id = id
        self.nombre = nombre
        self.horas_semanales = horas_semanales
        self.docentes_calificados = docentes_calificados
        self.ciclo = ciclo

    def asignar_docente(self, docente_id):
        if docente_id not in self.docentes_calificados:
            self.docentes_calificados.append(docente_id)
