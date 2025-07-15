from fastapi import APIRouter, HTTPException
from app.models.schemas import Cliente, OTPRequest, VerificarClienteRequest
from app.models.database import clientes_db
from typing import List
'''
Este modulo gestiona:
- Verificacion si el cliente ya se encuentra registrado
- Registra nuevo cliente
- Envia OTP (Opcional)
- Valida OTP (Opcional)
'''

router = APIRouter()

# # Simulación de base de datos en memoria
# clientes_simulados = {
#     "00000000": {"nombre": "Juan Simulado"}
# }

@router.post("/verificar")
def verificar_cliente(request: VerificarClienteRequest):
    if any(c["dni"] == request.dni for c in clientes_db):
        raise HTTPException(status_code=400, detail="Cliente ya registrado")
    return {"cliente_existente": False}

@router.post("/registrar")
def registrar_cliente(data: Cliente):
    if any(c["dni"] == data.dni for c in clientes_db):
        raise HTTPException(status_code=400, detail="Cliente ya registrado")
    clientes_db.append(data.dict())
    return {"mensaje": "Cliente registrado correctamente", "cliente": data}

@router.post("/otp/enviar")
def enviar_otp(request: VerificarClienteRequest):
    return {"mensaje": f"OTP enviado al número asociado con DNI {request.dni}", "otp": "123456"}

@router.post("/otp/validar")
def validar_otp(data: OTPRequest):
    if data.otp == "123456":
        return {"mensaje": "OTP validado correctamente"}
    raise HTTPException(status_code=400, detail="OTP incorrecto")

@router.get("/listar", response_model=List[Cliente])
def listar_clientes():
    return clientes_db