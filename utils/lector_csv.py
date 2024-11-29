import csv
from pathlib import Path
from typing import List

from models.aula import Aula
from models.curso import Curso
from models.docente import Docente
from models.turno import Turno


class LectorCSV:
    def __init__(self):
        # Ruta a la carpeta 'data' en la raíz del proyecto
        self.ruta_base = Path(__file__).parent.parent / "data"

        # Asegurarse de que la carpeta 'data' exista
        self.ruta_base.mkdir(parents=True, exist_ok=True)

    # Métodos de lectura
    def leer_aulas(self) -> List[Aula]:
        aulas = []
        with open(
            self.ruta_base / "aulas.csv", mode="r", newline="", encoding="utf-8"
        ) as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                aula = Aula(
                    id=fila["id"],
                    capacidad=int(fila["capacidad"]),
                    uso_especial=fila.get("uso_especial", None),
                )
                aulas.append(aula)
        return aulas

    def leer_cursos(self) -> List[Curso]:
        cursos = []
        with open(
            self.ruta_base / "cursos.csv", mode="r", newline="", encoding="utf-8"
        ) as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                curso = Curso(
                    id=fila["id"],
                    nombre=fila["nombre"],
                    horas_semanales=int(fila["horas_semanales"]),
                    docentes_calificados=fila["docentes_calificados"].split(";"),
                    ciclo=fila["ciclo"],
                )
                cursos.append(curso)
        return cursos

    def leer_docentes(self) -> List[Docente]:
        docentes = []
        with open(
            self.ruta_base / "docentes.csv", mode="r", newline="", encoding="utf-8"
        ) as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                docente = Docente(
                    id=fila["id"],
                    nombre=fila["nombre"],
                    tipo=fila["tipo"],
                    disponibilidad=fila["disponibilidad"].split(";"),
                    horas_max=int(fila["horas_max"]),
                    horas_min=int(fila["horas_min"]),
                )
                docentes.append(docente)
        return docentes

    def leer_turnos(self) -> List[Turno]:
        turnos = []
        with open(
            self.ruta_base / "turnos.csv", mode="r", newline="", encoding="utf-8"
        ) as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                turno = Turno(
                    id=fila["id"],
                    nombre=fila["nombre"],
                    horario_disponible={
                        "inicio": fila["horario_inicio"],
                        "fin": fila["horario_fin"],
                    },
                )
                turnos.append(turno)
        return turnos

    # Métodos de escritura
    def guardar_aulas(self, aulas: List[Aula]):
        with open(
            self.ruta_base / "aulas.csv", mode="w", newline="", encoding="utf-8"
        ) as archivo:
            campos = ["id", "capacidad", "uso_especial"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for aula in aulas:
                escritor.writerow(
                    {
                        "id": aula.id,
                        "capacidad": aula.capacidad,
                        "uso_especial": aula.uso_especial or "",
                    }
                )

    def guardar_cursos(self, cursos: List[Curso]):
        with open(
            self.ruta_base / "cursos.csv", mode="w", newline="", encoding="utf-8"
        ) as archivo:
            campos = [
                "id",
                "nombre",
                "horas_semanales",
                "docentes_calificados",
                "ciclo",
            ]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for curso in cursos:
                escritor.writerow(
                    {
                        "id": curso.id,
                        "nombre": curso.nombre,
                        "horas_semanales": curso.horas_semanales,
                        "docentes_calificados": ";".join(curso.docentes_calificados),
                        "ciclo": curso.ciclo,
                    }
                )

    def guardar_docentes(self, docentes: List[Docente]):
        with open(
            self.ruta_base / "docentes.csv", mode="w", newline="", encoding="utf-8"
        ) as archivo:
            campos = [
                "id",
                "nombre",
                "tipo",
                "disponibilidad",
                "horas_max",
                "horas_min",
            ]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for docente in docentes:
                escritor.writerow(
                    {
                        "id": docente.id,
                        "nombre": docente.nombre,
                        "tipo": docente.tipo,
                        "disponibilidad": ";".join(docente.disponibilidad),
                        "horas_max": docente.horas_max,
                        "horas_min": docente.horas_min,
                    }
                )

    def guardar_turnos(self, turnos: List[Turno]):
        with open(
            self.ruta_base / "turnos.csv", mode="w", newline="", encoding="utf-8"
        ) as archivo:
            campos = ["id", "nombre", "horario_inicio", "horario_fin"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for turno in turnos:
                escritor.writerow(
                    {
                        "id": turno.id,
                        "nombre": turno.nombre,
                        "horario_inicio": turno.horario_disponible["inicio"],
                        "horario_fin": turno.horario_disponible["fin"],
                    }
                )
