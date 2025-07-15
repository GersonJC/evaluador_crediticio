# database.py
from faker import Faker
from datetime import datetime, timedelta
import random
from app.models.schemas import Genero, EstadoCivil
from collections import deque

fake = Faker('es_ES')

def generar_clientes(n: int = 20) -> list[dict]:
    clientes = []
    for _ in range(n):
        clientes.append({
            "nombre_completo": fake.name(),
            "dni": str(fake.unique.random_number(digits=8)),
            "fecha_nacimiento": (datetime.now() - timedelta(days=random.randint(18*365, 70*365))).strftime("%Y-%m-%d"),
            "genero": random.choice(["Masculino", "Femenino"]),
            "estado_civil": random.choice(list(EstadoCivil.__members__.values())),
            "direccion": fake.address(),
            "telefono": fake.phone_number(),
            "email": fake.email()
        })
    return clientes

clientes_db = [] #generar_clientes(20)
solicitudes_db = []
solicitudes_urgentes = []  # Pila (LIFO)
cola_evaluacion = deque()  # Cola (FOFI)

def agregar_solicitud(solicitud):
    solicitudes_db.append(solicitud)
    cola_evaluacion.append(solicitud)  # FIFO
    if solicitud["urgente"]:
        solicitudes_urgentes.append(solicitud)  # LIFO