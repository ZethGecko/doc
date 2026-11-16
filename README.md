# CRUD de Ejemplos – FastAPI + Swagger + Render

API REST desarrollada con **FastAPI** que implementa un CRUD básico de “ejemplos”, con validación mediante **Pydantic v2**, documentación interactiva generada automáticamente con **Swagger UI**, y despliegue en **Render** como Web Service.

## 📋 Tabla de contenidos
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación local](#instalación-local)
- [Ejecución local](#ejecución-local)
- [Versionado de datos (esquema)](#versionado-de-datos-esquema)
- [Despliegue en Render](#despliegue-en-render)
- [Endpoints](#endpoints)
- [Limitaciones del plan gratuito](#limitaciones-del-plan-gratuito)
- [Reproducibilidad](#reproducibilidad)

## Características
- CRUD completo de “ejemplos”.
- Validación de entrada con Pydantic v2 (`min_length`, `max_length`, `ge`).
- Middleware CORS para permitir consumo desde cualquier origen.
- Documentación interactiva en `/docs` (Swagger UI) y `/redoc`.
- Persistencia en SQLite mediante SQLAlchemy (lista para migrar a PostgreSQL).
- Preparado para ejecutarse en Render con `uvicorn`.

## Requisitos
- Python 3.10 o superior.
- Cuenta en GitHub.
- Cuenta en Render (plan gratuito suficiente para la demo).

## Instalación local
```bash
git clone https://github.com/[tu-usuario]/fastapi-crud.git
cd fastapi-crud
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt