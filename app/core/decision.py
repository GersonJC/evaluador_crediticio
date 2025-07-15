'''
Matriz de desiciones
'''

def tomar_decision(score: int, monto: float):
    if score >= 850 and monto <= 10000:
        return {"estado": "Aprobación inmediata", "proceso": "Digital"}
    elif score >= 750 and monto <= 5000:
        return {"estado": "Auto-aprobación", "proceso": "Digital"}
    elif score >= 650 and monto <= 3000:
        return {"estado": "Pre-aprobación", "proceso": "Digital + call center"}
    elif score >= 500 and monto <= 5000:
        return {"estado": "Evaluación manual", "proceso": "Digital + videollamada"}
    elif score >= 400:
        return {"estado": "Evaluación completa", "proceso": "Híbrido"}
    else:
        return {"estado": "Rechazo automático", "proceso": "Digital"}