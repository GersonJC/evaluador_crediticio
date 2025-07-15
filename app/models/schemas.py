from pydantic import BaseModel, EmailStr
from datetime import date
from enum import Enum

class Genero(str, Enum):
    MASCULINO = "Masculino"
    FEMENINO = "Femenino"

class EstadoCivil(str, Enum):
    SOLTERO = "Soltero/a"
    CASADO = "Casado/a"
    DIVORCIADO = "Divorciado/a"
    VIUDO = "Viudo/a"

class TipoEmpleo(str, Enum):
    DEPENDIENTE = "Dependiente"
    INDEPENDIENTE = "Independiente"

class Cliente(BaseModel):
    nombre_completo: str
    dni: str
    fecha_nacimiento: date
    genero: Genero
    estado_civil: EstadoCivil
    direccion: str
    telefono: str
    email: EmailStr

class OTPRequest(BaseModel):
    dni: str
    otp: str

# class SolicitudResumenRequest(BaseModel):
#     dni: str
#     monto: float

class DatosLaborales(BaseModel):
    tipo_empleo: TipoEmpleo
    nombre_empresa: str = None
    salario: float = None
    ingresos: float = None
    egresos: float = None
    patrimonio: float = None
    bienes: list[str] = None

class SolicitudRequest(BaseModel):
    dni_cliente: str
    monto: float
    plazo_meses: int
    urgente: bool = False
    datos_laborales: DatosLaborales
    # ingresos: float
    # egresos: float
    # dependientes: int

class EvaluacionRequest(BaseModel):
    dni_cliente: str
    # ingresos: float
    # egresos: float
    # dependientes: int
    # monto: float

class VerificarClienteRequest(BaseModel):
    dni: str

# class FirmaContratoRequest(BaseModel):
#     acepta: bool

# class DesembolsoRequest(BaseModel):
#     cuenta_bancaria: str

class DesembolsoRequest(BaseModel):
    cuenta_bancaria: str
    dni: str
    monto: float
