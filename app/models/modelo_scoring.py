from sklearn.ensemble import RandomForestRegressor
import numpy as np
import joblib

# Datos sintéticos para entrenamiento (ejemplo)
def generar_datos_entrenamiento(n: int = 1000) -> tuple:
    X = np.array([
        np.random.uniform(1000, 10000, n),  # ingresos
        np.random.uniform(500, 8000, n),     # egresos
        # np.random.randint(0, 5, n),          # dependientes
        np.random.randint(1, 6, n)           # historial_crediticio (1-5)
    ]).T
    y = X[:, 0] * 0.6 - X[:, 1] * 0.3 - X[:, 2] * 100 + (6 - X[:, 2]) * 50  # Fórmula base
    return X, y

# Entrenar y guardar el modelo (ejecutar una vez)
def entrenar_modelo():
    X, y = generar_datos_entrenamiento()
    model = RandomForestRegressor(n_estimators=50).fit(X, y)
    joblib.dump(model, "modelo_scoring.pkl")

