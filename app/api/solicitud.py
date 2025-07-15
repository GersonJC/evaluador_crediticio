
from fastapi import APIRouter, HTTPException
from app.models.schemas import SolicitudRequest
from app.models.database import solicitudes_db, clientes_db, solicitudes_urgentes, cola_evaluacion

'''
Este modulo gestiona:
- El registo de una solicitud resumen de un cliente
- Completa los detalles de la solicitud
'''

router = APIRouter()

@router.post("/crear")
def crear_solicitud(solicitud: SolicitudRequest):
    solicitudes_db.append(solicitud.dict())
    if solicitud.urgente:
        solicitudes_urgentes.append(solicitud.dict())
    else:
        cola_evaluacion.append(solicitud.dict())
    return {"mensaje": "Solicitud creada"}

    # if not any(c["dni"] == solicitud.dni_cliente for c in clientes_db):
    #     raise HTTPException(status_code=404, detail="Cliente no encontrado")
    # solicitudes_db.append(solicitud.dict())
    # return solicitud


# # Simulador de almacenamiento en memoria
# solicitudes_temporales = {}

# # --- Registro preliminar de la solicitud ---
# @router.post("/resumen")
# def solicitud_resumen(data: SolicitudResumenRequest):
#     # Guardamos datos básicos en memoria (simulado)
#     solicitudes_temporales[data.dni] = {
#         "dni": data.dni,
#         "monto": data.monto
#     }
#     return {
#         "mensaje": "Solicitud preliminar registrada",
#         "datos": solicitudes_temporales[data.dni]
#     }

# # --- Registro de detalles para evaluación ---
# @router.post("/detalle")
# def solicitud_detalle(data: SolicitudDetalleRequest):
#     # Suponemos que ya se hizo el paso anterior
#     dni = data.dni
#     if dni not in solicitudes_temporales:
#         return {"error": "Primero debe registrar una solicitud resumida"}

#     # Agregamos los datos adicionales
#     solicitudes_temporales[dni].update({
#         "ingresos": data.ingresos,
#         "egresos": data.egresos,
#         "dependientes": data.dependientes
#     })

#     return {
#         "mensaje": "Solicitud detallada completada",
#         "datos_completos": solicitudes_temporales[dni]
#     }