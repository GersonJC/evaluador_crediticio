from fastapi import APIRouter, HTTPException
from app.models.schemas import EvaluacionRequest, SolicitudRequest, TipoEmpleo
from app.models.database import solicitudes_db, clientes_db
from app.core.scoring import calcular_scoring_ml
from app.core.decision import tomar_decision
# from app.core.scoring import calcular_scoring
# from app.core.decision import tomar_decision

'''
Este modulo gestiona:
- El calculo del score crediticio
- La desicion automatica
'''

router = APIRouter()

@router.post("/")
def evaluar_credito(data: EvaluacionRequest):
    #print(solicitudes_db)

    solicitudes_clientes = [
        s for s in solicitudes_db
        if s.get("dni_cliente") == data.dni_cliente
    ]
    if not solicitudes_clientes:
        raise HTTPException(
            status_code=400,
            detail= f"No se encontraron solicitudes para el DNI {data.dni_cliente}"
            )
    ultima_solicitud = solicitudes_clientes[-1]

    datos_laborales = ultima_solicitud.get("datos_laborales", {})

    if not datos_laborales:
        raise HTTPException(
            status_code=400,
            detail="La solicitud no tiene datos laborales registrados"
        )
    
    p_meses = ultima_solicitud.get("plazo_meses",0)

    if datos_laborales["tipo_empleo"] == TipoEmpleo.DEPENDIENTE:
        ingresos = datos_laborales.get("salario",0)
        egresos = 1
        
    else:
        ingresos = datos_laborales.get("ingresos",0)
        egresos = datos_laborales.get("egresos", 0)
    
    try:

        score = calcular_scoring_ml({
            "ingresos": ingresos,
            "egresos": egresos,
            "historial_crediticio": 3  
        })
        
        decision = tomar_decision(
            score, 
            ultima_solicitud["monto"]
            )
        
        #solicitud_id = ultima_solicitud.get("id", "N/A") 

        capd_pago = capacidad_pago(
            ingresos, 
            egresos, 
            #ultima_solicitud.get("plazo_meses", 0)
            p_meses
            )

        return {
            "success": True,
            "dni": data.dni_cliente,
            "score": score,
            "decision": decision,
            "capacidad": capd_pago 
            #"solicitud_usada": solicitud_id
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al calcular scoring: {str(e)}"
        )

def capacidad_pago(ingresos, egresos, meses):
    if meses == 0: return ingresos - egresos
    return (ingresos - egresos) + capacidad_pago(ingresos, egresos, meses-1)

    # solicitud = next((s for s in solicitudes_db if s["dni_cliente"] == data.dni_cliente), None)
    # if not solicitud:
    #     raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    
    # datos_laborales = solicitud["datos_laborales"]
    
    # if datos_laborales["tipo_empleo"] == TipoEmpleo.DEPENDIENTE:
    #     ingresos = datos_laborales.get("salario",0)
    # else:
    #     ingresos = datos_laborales.get("ingresos",0)

    # score = calcular_scoring_ml({
    #     "ingresos": ingresos,
    #     "egresos": datos_laborales.get("egresos",0),
    #     "historial_crediticio": 3
    # })

    # #score = calcular_scoring(data)
    # decision = tomar_decision(score, solicitud["monto"])
    # return {
    #     "score": score, 
    #     "decision": decision,
    #     "tipo_empleo": datos_laborales["tipo_empleo"]
    #     }