from fastapi import APIRouter, Request
from app.models.schemas import DesembolsoRequest

'''
Este modulo gestiona:
- El calculo del score crediticio
- La desicion automatica
'''

router = APIRouter()

@router.post("/")
def evaluar_credito(data: DesembolsoRequest, request: Request):

    clientes_array = request.app.state.clientes_array
    ## Devuelve TRUE si encuentra al cliente por DNI
    encontrado = any(cliente["dni"] == data.dni for cliente in clientes_array)

    cuenta_bancaria = data.cuenta_bancaria
    dni = data.dni
    monto = data.monto

    if encontrado:
        return {
            "mensaje": f"Se ha hecho el desembolso con éxito de S/{monto} a la cuenta {cuenta_bancaria}  del titular con DNI: {dni}"
        }

    if not encontrado:
        return {"error": "Primero debe registrar al cliente"}