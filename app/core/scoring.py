
'''
Calcula un puntaje crediticio 
'''

# def calcular_scoring(data):
#     # Fórmula simple: ingresos - egresos - dependientes*300
#     base = data.ingresos - data.egresos - (data.dependientes * 300)
#     score = max(0, min(500, int(base / 10)))
#     return score

# from sklearn.ensemble import RandomForestRegressor
# import numpy as np
import joblib
from app.models.modelo_scoring import entrenar_modelo

# Cargar modelo preentrenado
try:
    modelo = joblib.load("modelo_scoring.pkl")
except:
    entrenar_modelo()
    modelo = joblib.load("modelo_socoring.pkl")

def calcular_scoring_ml(data: dict) -> int:
    input_data = [[
        data["ingresos"],
        data["egresos"],
        #data["dependientes"],
        data["historial_crediticio"]
    ]]
    raw_score = modelo.predict(input_data)[0]

    score = max(300, min(850, int(raw_score)))
    
    # Ajustar para evitar scores demasiado altos sin razón
    if score > 800 and data["egresos"] > data["ingresos"] * 0.5:
        score -= 100  # Penalizar si los egresos son altos

    return score

