from fastapi import APIRouter
from app.api import cliente, solicitud, evaluacion, desembolso

router = APIRouter()

router.include_router(cliente.router, prefix="/cliente", tags=["Cliente"])
router.include_router(solicitud.router, prefix="/solicitud", tags=["Solicitud"])
router.include_router(evaluacion.router, prefix="/evaluar", tags=["Evaluación"])
##router.include_router(contrato.router, prefix="/contrato", tags=["Contrato"])
router.include_router(desembolso.router, prefix="/desembolso", tags=["Desembolso"])
