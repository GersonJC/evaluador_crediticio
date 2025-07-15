from fastapi import APIRouter
from app.models.database import clientes_db, solicitudes_db
from app.core.algoritmos import merge_sort

router = APIRouter()

@router.get("/preaprobados")
def reporte_preaprobados():
    clientes_ordenados = merge_sort(clientes_db, key="score")
    return [c for c in clientes_ordenados if c["score"] >= 700]

@router.get("/por-monto/{min_monto}")
def reporte_por_monto(min_monto: float):
    solicitudes_ordenadas = merge_sort(solicitudes_db, key="monto")
    return [s for s in solicitudes_ordenadas if s["monto"] >= min_monto]