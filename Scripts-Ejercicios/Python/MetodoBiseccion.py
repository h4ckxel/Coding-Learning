import math

def numero_minimo_iteraciones_biseccion(a, b, potenciaDiez=1e-3):
    # calcula numero de iteraciones
    n = math.log2((b - a) / potenciaDiez)
    return math.ceil(n)  # redondeo

# Intervalo (a, b)
a = 3.2
b = 4.0
iteraciones = numero_minimo_iteraciones_biseccion(a, b)
print(f"Número mínimo de iteraciones: {iteraciones}")