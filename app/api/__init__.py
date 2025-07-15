from fastapi import APIRouter
from app.api import cliente, solicitud, evaluacion, reportes, desembolso

router = APIRouter()

router.include_router(cliente.router, prefix="/cliente", tags=["Cliente"])
router.include_router(solicitud.router, prefix="/solicitud", tags=["Solicitud"])
router.include_router(evaluacion.router, prefix="/evaluar", tags=["Evaluación"])
router.include_router(reportes.router, prefix="/reportes", tags=["Reportes"])
router.include_router(desembolso.router, prefix="/desembolso", tags=["Desembolso"])
