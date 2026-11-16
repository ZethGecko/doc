from typing import Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="CRUD de Ejemplos",
    description="API FastAPI con CRUD básico y documentación Swagger en /docs",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class MensajeRespuesta(BaseModel):
    detail: str


class EjemploCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    valor: Optional[float] = Field(None, ge=0)


class Ejemplo(EjemploCreate):
    id: int


_db: List[Ejemplo] = []
_next_id = 1


@app.get("/")
def root():
    return {"message": "API FastAPI CRUD activa. Documentación: /docs"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ejemplos", response_model=List[Ejemplo])
def listar_ejemplos():
    return _db


@app.get("/ejemplos/{ejemplo_id}", response_model=Ejemplo)
def obtener_ejemplo(ejemplo_id: int):
    for item in _db:
        if item.id == ejemplo_id:
            return item
    raise HTTPException(status_code=404, detail="Ejemplo no encontrado")


@app.post("/ejemplos", response_model=Ejemplo, status_code=201)
def crear_ejemplo(data: EjemploCreate):
    global _next_id
    item = Ejemplo(id=_next_id, nombre=data.nombre, valor=data.valor)
    _db.append(item)
    _next_id += 1
    return item


@app.put("/ejemplos/{ejemplo_id}", response_model=Ejemplo)
def actualizar_ejemplo(ejemplo_id: int, data: EjemploCreate):
    for idx, item in enumerate(_db):
        if item.id == ejemplo_id:
            actualizado = Ejemplo(id=ejemplo_id, nombre=data.nombre, valor=data.valor)
            _db[idx] = actualizado
            return actualizado
    raise HTTPException(status_code=404, detail="Ejemplo no encontrado")


@app.delete("/ejemplos/{ejemplo_id}", response_model=MensajeRespuesta)
def eliminar_ejemplo(ejemplo_id: int):
    for idx, item in enumerate(_db):
        if item.id == ejemplo_id:
            _db.pop(idx)
            return {"detail": "Ejemplo eliminado"}
    raise HTTPException(status_code=404, detail="Ejemplo no encontrado")