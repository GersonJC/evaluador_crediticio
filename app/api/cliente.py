from fastapi import APIRouter, HTTPException
from app.models.schemas import RegistroClienteRequest, OTPRequest, VerificarClienteRequest

'''
Este modulo gestiona:
- Verificacion si el cliente ya se encuentra registrado
- Registra nuevo cliente
- Envia OTP (Opcional)
- Valida OTP (Opcional)
'''

router = APIRouter()

# Simulación de base de datos en memoria
clientes_simulados = {
    "00000000": {"nombre": "Juan Simulado"}
}

@router.post("/verificar")
def verificar_cliente(request: VerificarClienteRequest):
    if request.dni == clientes_simulados:
        return {"cliente_existente": True}
    return {"cliente_existente": False}

@router.post("/registrar")
def registrar_cliente(data: RegistroClienteRequest):
    return {"mensaje": "Cliente registrado correctamente", "cliente": data}

@router.post("/otp/enviar")
def enviar_otp(request: VerificarClienteRequest):
    return {"mensaje": f"OTP enviado al número asociado con DNI {request.dni}", "otp": "123456"}

@router.post("/otp/validar")
def validar_otp(data: OTPRequest):
    if data.otp == "123456":
        return {"mensaje": "OTP validado correctamente"}
    raise HTTPException(status_code=400, detail="OTP incorrecto")
