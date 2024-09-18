import math

def numero_minimo_iteraciones_biseccion(a, b, potenciaDiez=1e-4):
    # calcula numero de iteraciones
    n = math.log2((b - a) / potenciaDiez)
    return math.ceil(n)  # redondeo

# Intervalo (a, b)
a = 0.0
b = 1.0
iteraciones = numero_minimo_iteraciones_biseccion(a, b)
print(f"Número mínimo de iteraciones: {iteraciones}")