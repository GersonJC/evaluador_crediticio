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

clientes_array = [
    {"dni": "00000000", "nombre": "Juan Simulado", "telefono": "", "email": ""}
]

cola_otp = [] 


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
    
    resp = verificar_cliente(request)
    if not resp.get("cliente_existente"):
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    codigo = "123456"
    cola_otp.append({"dni": request.dni, "otp": codigo}) 

    return {"mensaje": f"OTP enviado al cliente con DNI {request.dni}", "otp": codigo}
    """return {"mensaje": f"OTP enviado al número asociado con DNI {request.dni}", "otp": "123456"}"""
@router.post("/otp/validar")
def validar_otp(data: OTPRequest):
    
    def buscar_y_validar(queue):
        if not queue:
            return False
        item = queue.pop(0) 
        if item["dni"] == data.dni and item["otp"] == data.otp:
            return True
        return buscar_y_validar(queue)

    valid = buscar_y_validar(cola_otp)
    if valid:
        return {"mensaje": "OTP validado correctamente"}
    """if data.otp == "123456":
        return {"mensaje": "OTP validado correctamente"}"""
    raise HTTPException(status_code=400, detail="OTP incorrecto")

@router.get("/listar", response_model=List[Cliente])
def listar_clientes():
    return clientes_db