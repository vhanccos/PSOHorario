from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers import aulas, cursos, docentes, turnos
from utils.lector_csv import LectorCSV

app = FastAPI()

# Configuración de Jinja2 y archivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar lector de CSV
lector = LectorCSV()

# Incluir las rutas de cada modelo
app.include_router(aulas.router, prefix="/aulas", tags=["Aulas"])
app.include_router(cursos.router, prefix="/cursos", tags=["Cursos"])
app.include_router(docentes.router, prefix="/docentes", tags=["Docentes"])
app.include_router(turnos.router, prefix="/turnos", tags=["Turnos"])


# Ruta principal para servir la página de inicio
@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Ruta para la página de aulas
@app.get("/aulas", response_class=HTMLResponse)
async def get_aulas(request: Request):
    aulas = lector.leer_aulas()
    return templates.TemplateResponse(
        "aulas.html", {"request": request, "aulas": aulas}
    )


# Ruta para la página de cursos
@app.get("/cursos", response_class=HTMLResponse)
async def get_cursos(request: Request):
    cursos = lector.leer_cursos()
    return templates.TemplateResponse(
        "cursos.html", {"request": request, "cursos": cursos}
    )


# Ruta para la página de docentes
@app.get("/docentes", response_class=HTMLResponse)
async def get_docentes(request: Request):
    docentes = lector.leer_docentes()
    return templates.TemplateResponse(
        "docentes.html", {"request": request, "docentes": docentes}
    )


# Ruta para la página de turnos
@app.get("/turnos", response_class=HTMLResponse)
async def get_turnos(request: Request):
    turnos = lector.leer_turnos()
    return templates.TemplateResponse(
        "turnos.html", {"request": request, "turnos": turnos}
    )
