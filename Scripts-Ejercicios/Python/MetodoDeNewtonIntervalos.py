# -*- coding: utf-8 -*-
"""
|--------------------------------------------------|
|----------------METODO DE NEWTON-RAPHSON----------|
|--------------------------------------------------|
"""

import numpy as np
import math
import pandas as pd

# definimos la función y su derivada
funcionx = lambda x: x**3 + 3*x**2 - 1  # f(x) = x^3 + 3x^2 - 1
derivada_funcionx = lambda x: 3*x**2 + 6*x  # f'(x) = 3x^2 + 6x

# función para convertir las entradas a valores numéricos (reconoce "pi")
def convertir_entrada(entrada):
    # reemplaza "pi" por "math.pi" y evalúa la expresión
    return eval(entrada.replace("pi", "math.pi"))

# solicita el número de intervalos al usuario
num_intervalos = int(input("número de intervalos a analizar: "))
intervalos = []  # almacena los intervalos ingresados

# solicita cada intervalo en el formato 'a b'
for i in range(num_intervalos):
    intervalo = input(f"intervalo {i+1} en formato 'a b' (ejemplo: -pi 2, pi 3*pi/2): ")
    # convierte cada parte del intervalo a un valor numérico usando `convertir_entrada`
    a, b = map(convertir_entrada, intervalo.split())
    intervalos.append([a, b])  # guarda el intervalo como [a, b]

# solicita la precisión (potencia de diez)
potenciaDeDiez = float(input("valor de la exactitud (ejemplo, 1e-5): "))
tabla = []  # almacena los resultados en forma de tabla

# aplica el método de newton-raphson para cada intervalo
for intervalo in intervalos:
    a, b = intervalo  # desempaqueta los límites del intervalo
    punto_inicial = (a + b) / 2  # usa el punto medio como punto inicial
    x_n = punto_inicial
    i = 1  # inicializa el contador de iteraciones
    
    print(f"------------------------------------------------\nintervalo: [{a}, {b}]\npunto inicial: {punto_inicial}")
    
    while True:
        f_xn = funcionx(x_n)  # calcula f(x_n)
        f_prime_xn = derivada_funcionx(x_n)  # calcula f'(x_n)

        # verifica que la derivada no sea cero para evitar errores de división
        if f_prime_xn == 0:
            print(f"la derivada se anuló en x = {x_n}, no se puede continuar.\n------------------------------------------------")
            break

        # calcula el siguiente punto usando la fórmula de newton-raphson
        x_n1 = x_n - (f_xn / f_prime_xn)

        # guarda la información de la iteración en la tabla
        tabla.append([i, a, b, x_n, f_xn, f_prime_xn, x_n1])

        # comprueba si la diferencia entre iteraciones es menor que la precisión deseada
        if abs(x_n1 - x_n) < potenciaDeDiez:
            print(f"convergencia alcanzada después de {i} iteraciones.\nraíz aproximada: {x_n1}\n------------------------------------------------")
            break

        # actualiza x_n para la siguiente iteración
        x_n = x_n1
        i += 1

# crea un dataframe con la tabla de resultados
df = pd.DataFrame(tabla, columns=["iteración", "intervalo a", "intervalo b", "x_n", "f(x_n)", "f'(x_n)", "x_n+1"])

# guarda la tabla en un archivo excel
df.to_excel("resultado_newton_raphson_intervalos.xlsx", index=False, engine='openpyxl')
print("archivo guardado con el nombre 'resultado_newton_raphson_intervalos.xlsx'")
