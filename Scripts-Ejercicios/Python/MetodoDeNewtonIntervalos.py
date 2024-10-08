# -*- coding: utf-8 -*-
"""
|--------------------------------------------------|
|----------------METODO DE NEWTON-RAPHSON----------|
|--------------------------------------------------|
"""

import numpy as np
import math
import pandas as pd

# Definimos la función y su derivada
funcionx = lambda x: x**3 + 3*x**2 - 1 # f(x) = x - cos(x)
derivada_funcionx = lambda x: 3*x**2 + 6*x # f'(x) = 1 + sin(x)

# Función para convertir las entradas en valores numéricos (reconoce "pi")
def convertir_entrada(entrada):
    # Reemplaza "pi" por "math.pi" y evalúa la expresión
    return eval(entrada.replace("pi", "math.pi"))

# Solicita el número de intervalos al usuario
num_intervalos = int(input("Número de intervalos a analizar: "))
intervalos = []  # Almacena los intervalos

# Solicita cada intervalo en el formato 'a b'
for i in range(num_intervalos):
    intervalo = input(f"Intervalo {i+1} en formato 'a b' (ejemplo: -pi 2, pi 3*pi/2): ")
    # Separa la entrada y convierte cada parte usando la función `convertir_entrada`
    a, b = map(convertir_entrada, intervalo.split())  # Convierte los valores en float con pi
    intervalos.append([a, b])  # Guarda cada intervalo como [a, b]

# Precisión (potencia de diez)
potenciaDeDiez = float(input("Valor de la exactitud (ejemplo, 1e-5): "))  # 1e-5 = 10^-5
tabla = []  # Almacena los resultados de la tabla

# Aplicamos el método de Newton-Raphson para cada intervalo
for intervalo in intervalos:
    a, b = intervalo  # Desempaquetamos los límites del intervalo
    punto_inicial = (a + b) / 2  # Usamos el punto medio como punto inicial
    x_n = punto_inicial
    i = 1  # Inicializamos el contador de iteraciones
    
    print(f"------------------------------------------------\nIntervalo: [{a}, {b}]\nPunto inicial: {punto_inicial}")
    
    while True:
        f_xn = funcionx(x_n)  # Calcula f(x_n)
        f_prime_xn = derivada_funcionx(x_n)  # Calcula f'(x_n)

        # Evitar división por cero
        if f_prime_xn == 0:
            print(f"La derivada se anuló en x = {x_n}, no se puede continuar.\n------------------------------------------------")
            break

        # Calcula el siguiente punto usando la fórmula de Newton-Raphson
        x_n1 = x_n - (f_xn / f_prime_xn)

        # Guarda la información de la iteración en la tabla
        tabla.append([i, a, b, x_n, f_xn, f_prime_xn, x_n1])

        # Comprueba si la diferencia es menor que la precisión deseada
        if abs(x_n1 - x_n) < potenciaDeDiez:
            print(f"Convergencia alcanzada después de {i} iteraciones.\nRaíz aproximada: {x_n1}\n------------------------------------------------")
            break

        # Actualiza x_n para la siguiente iteración
        x_n = x_n1
        i += 1

# Crear un DataFrame con la tabla de resultados
df = pd.DataFrame(tabla, columns=["Iteración", "Intervalo a", "Intervalo b", "x_n", "f(x_n)", "f'(x_n)", "x_n+1"])

# Guardar la tabla en un archivo Excel
df.to_excel("resultado_newton_raphson_intervalos.xlsx", index=False, engine='openpyxl')
print("Nombre del archivo 'resultado_newton_raphson_intervalos.xlsx'")
