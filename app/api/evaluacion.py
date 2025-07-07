from fastapi import APIRouter
from app.models.schemas import EvaluacionRequest
from app.core.scoring import calcular_scoring
from app.core.decision import tomar_decision

'''
Este modulo gestiona:
- El calculo del score crediticio
- La desicion automatica
'''

router = APIRouter()

@router.post("/")
def evaluar_credito(data: EvaluacionRequest):
    score = calcular_scoring(data)
    decision = tomar_decision(score, data.monto)
    return {"score": score, "decision": decision}