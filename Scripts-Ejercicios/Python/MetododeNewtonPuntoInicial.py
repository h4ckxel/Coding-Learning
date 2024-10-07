# -*- coding: utf-8 -*-
"""
|--------------------------------------------------|
|----------------METODO DE NEWTON-RAPHSON----------|
|----------------------PUNTO INICIAL---------------|
"""

import numpy as np
import math
import pandas as pd

# Definimos la función y su derivada
funcionx = lambda x: -x**3 - math.cos(x)  # f(x) = x^2 - 3
derivada_funcionx = lambda x: -3 * x**2 + math.sin(x)  # f'(x) = 2x

# Número de intervalos (inicializaciones)
num_intervalos = int(input("Número de puntos iniciales a analizar: "))
puntos_iniciales = []

# Solicita los puntos iniciales al usuario
for i in range(num_intervalos):
    punto_inicial = float(input(f"Punto inicial {i+1} (ejemplo: 1.5): "))
    puntos_iniciales.append(punto_inicial)  # guarda cada punto inicial

# Precisión (potencia de diez)
potenciaDeDiez = float(input("Valor de la exactitud (ejemplo, 1e-5): "))  # 1e-5 = 10^-5
tabla = []  # Almacena los resultados de la tabla

# Aplicamos el método de Newton-Raphson para cada punto inicial
for punto_inicial in puntos_iniciales:
    x_n = punto_inicial
    i = 1
    print(f"------------------------------------------------\nPunto inicial: {punto_inicial}")
    while True:
        f_xn = funcionx(x_n)
        f_prime_xn = derivada_funcionx(x_n)

        # Evitar división por cero
        if f_prime_xn == 0:
            print(f"La derivada se anuló en x = {x_n}, no se puede continuar.\n------------------------------------------------")
            break

        # Calcula el siguiente punto usando la fórmula de Newton-Raphson
        x_n1 = x_n - (f_xn / f_prime_xn)

        # Guarda la información de la iteración
        tabla.append([i, x_n, f_xn, f_prime_xn, x_n1])

        # Comprueba si la diferencia es menor que la precisión deseada
        if abs(x_n1 - x_n) < potenciaDeDiez:
            print(f"Convergencia alcanzada después de {i} iteraciones.\nRaíz aproximada: {x_n1}\n------------------------------------------------")
            break

        # Actualiza x_n para la siguiente iteración
        x_n = x_n1
        i += 1

# DataFrame con la tabla para guardar en Excel
df = pd.DataFrame(tabla, columns=["Iteración", "x_n", "f(x_n)", "f'(x_n)", "x_n+1"])

# Guardar en archivo Excel
df.to_excel("resultado_newton_raphson.xlsx", index=False, engine='openpyxl')
print("Nombre del archivo 'resultado_newton_raphson.xlsx'")

