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

clientes_array = [
    {"dni": "00000000", "nombre": "Juan Simulado", "telefono": "", "email": ""}
]

cola_otp = [] 


# Simulación de base de datos en memoria
"""
clientes_simulados = {
    "00000000": {"nombre": "Juan Simulado"}
}"""

@router.post("/verificar")
def verificar_cliente(request: VerificarClienteRequest):
    
    stack_auxiliar = []
    encontrado = False
    
    while clientes_array:
        cliente = clientes_array.pop(0) 
        stack_auxiliar.append(cliente)    
        if cliente["dni"] == request.dni:
            encontrado = True
    
    while stack_auxiliar:
        clientes_array.insert(0, stack_auxiliar.pop())

    return {"cliente_existente": encontrado}
    
    """
    if request.dni == clientes_simulados:
        return {"cliente_existente": True}
    return {"cliente_existente": False}
    """
@router.post("/registrar")
def registrar_cliente(data: RegistroClienteRequest):
  
    for c in clientes_array:
        if c["dni"] == data.dni:
            raise HTTPException(status_code=400, detail="Cliente ya registrado")

    nuevo_cliente = {
        "dni": data.dni,
        "nombre": data.nombre,
        "telefono": data.telefono,
        "email": data.email
    }
    clientes_array.append(nuevo_cliente)

    return {"mensaje": "Cliente registrado correctamente", "cliente": nuevo_cliente}

    """return {"mensaje": "Cliente registrado correctamente", "cliente": data}"""

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
