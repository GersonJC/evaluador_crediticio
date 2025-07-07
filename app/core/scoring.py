
'''
Calcula un puntaje crediticio 
'''

def calcular_scoring(data):
    # Fórmula simple: ingresos - egresos - dependientes*300
    base = data.ingresos - data.egresos - (data.dependientes * 300)
    score = max(0, min(500, int(base / 10)))
    return score