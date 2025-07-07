
from fastapi import APIRouter
from app.models.schemas import SolicitudResumenRequest, SolicitudDetalleRequest

'''
Este modulo gestiona:
- El registo de una solicitud resumen de un cliente
- Completa los detalles de la solicitud
'''

router = APIRouter()

# Simulador de almacenamiento en memoria
solicitudes_temporales = {}

# --- Registro preliminar de la solicitud ---
@router.post("/resumen")
def solicitud_resumen(data: SolicitudResumenRequest):
    # Guardamos datos básicos en memoria (simulado)
    solicitudes_temporales[data.dni] = {
        "dni": data.dni,
        "monto": data.monto
    }
    return {
        "mensaje": "Solicitud preliminar registrada",
        "datos": solicitudes_temporales[data.dni]
    }

# --- Registro de detalles para evaluación ---
@router.post("/detalle")
def solicitud_detalle(data: SolicitudDetalleRequest):
    # Suponemos que ya se hizo el paso anterior
    dni = data.dni
    if dni not in solicitudes_temporales:
        return {"error": "Primero debe registrar una solicitud resumida"}

    # Agregamos los datos adicionales
    solicitudes_temporales[dni].update({
        "ingresos": data.ingresos,
        "egresos": data.egresos,
        "dependientes": data.dependientes
    })

    return {
        "mensaje": "Solicitud detallada completada",
        "datos_completos": solicitudes_temporales[dni]
    }