from utils.lector_csv import LectorCSV

# Crear una instancia del lector CSV
lector = LectorCSV()

# Leer los datos desde los archivos CSV
aulas = lector.leer_aulas()
cursos = lector.leer_cursos()
docentes = lector.leer_docentes()
turnos = lector.leer_turnos()

# Mostrar los datos leídos

print("Aulas:")
for aula in aulas:
    print(
        f"ID: {aula.id}, Capacidad: {aula.capacidad}, Uso especial: {aula.uso_especial}"
    )

print("\nCursos:")
for curso in cursos:
    print(
        f"ID: {curso.id}, Nombre: {curso.nombre}, Horas semanales: {curso.horas_semanales}, Ciclo: {curso.ciclo}"
    )
    print(f"Docentes calificados: {', '.join(curso.docentes_calificados)}")

print("\nDocentes:")
for docente in docentes:
    print(
        f"ID: {docente.id}, Nombre: {docente.nombre}, Tipo: {docente.tipo}, Horas max: {docente.horas_max}, Horas min: {docente.horas_min}"
    )
    print(f"Disponibilidad: {', '.join(docente.disponibilidad)}")

print("\nTurnos:")
for turno in turnos:
    print(
        f"ID: {turno.id}, Nombre: {turno.nombre}, Horario: {turno.horario_disponible['inicio']} - {turno.horario_disponible['fin']}"
    )
