'''
Matriz de desiciones
'''

def tomar_decision(score: int, monto: float):
    if score >= 450 and monto <= 2000:
        return {"estado": "Auto-aprobación", "proceso": "Digital"}
    elif 350 <= score <= 449 and monto <= 2000:
        return {"estado": "Pre-aprobación", "proceso": "Digital + call center"}
    elif score >= 400 and 2001 <= monto <= 5000:
        return {"estado": "Evaluación manual", "proceso": "Digital + videollamada"}
    elif 300 <= score <= 399 and 2001 <= monto <= 5000:
        return {"estado": "Evaluación completa", "proceso": "Híbrido"}
    elif score < 300:
        return {"estado": "Rechazo automático", "proceso": "Digital"}
    else:
        return {"estado": "Revisión manual", "proceso": "Revisión"}