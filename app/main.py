from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(
    title="Evaluador Crediticio Digital",
    description="API para evaluación crediticia automatizada",
    version="0.0.1"
    )

# Incluimos todas las rutas
app.include_router(api_router)

# @app.get("/")
# def root():
#     return {
#         "mensaje": "Bienvenido a la API de Evaluación Crediticia Digital",
#         "documentacion": "/docs",
#         "version": "1.0.0"
#     }