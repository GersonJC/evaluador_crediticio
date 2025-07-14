from pydantic import BaseModel, EmailStr

class RegistroClienteRequest(BaseModel):
    dni: str
    nombre: str
    telefono: str
    email: EmailStr

class OTPRequest(BaseModel):
    dni: str
    otp: str

class SolicitudResumenRequest(BaseModel):
    dni: str
    monto: float

class SolicitudDetalleRequest(BaseModel):
    dni: str
    ingresos: float
    egresos: float
    dependientes: int

class EvaluacionRequest(BaseModel):
    ingresos: float
    egresos: float
    dependientes: int
    monto: float

class VerificarClienteRequest(BaseModel):
    dni: str

# class FirmaContratoRequest(BaseModel):
#     acepta: bool

class DesembolsoRequest(BaseModel):
    cuenta_bancaria: str
    dni: str
    monto: float
