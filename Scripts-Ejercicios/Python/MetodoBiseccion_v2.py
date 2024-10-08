# -*- coding: utf-8 -*-
"""
|--------------------------------------------------|
|----------------METODO DE BISECCION---------------|
|--------------------------------------------------|
def numero_minimo_iteraciones_biseccion(a, b, potenciaDiez):
    # formula para calcular iteraciones
    n = math.log2((b - a) / potenciaDiez)
    return math.ceil(n)  # redondeo hacia arriba
"""

from MetodoBiseccion import numero_minimo_iteraciones_biseccion as iteraciones
import numpy as np
import math 
import pandas as pd
# funcion
funcionx = lambda x: x**2 - 3

# num de intervalos
num_intervalos = int(input("Número de intervalos a analizar: "))
intervalos = []

# se pide intervalos al usuario
for i in range(num_intervalos):
    intervalo = input(f"Intervalo {i+1} en formato 'a b' (ejemplo: -1.5 2.5): ")
    a, b = map(float, intervalo.split())  # convierte los valores separados en float
    intervalos.append([a, b])  # guarda el intervalo como [a, b]

# precisión (potencia de diez)
potenciaDeDiez = float(input("Valor de la exactitud (ejemplo, 1e-5): ")) # 1e-5 = 10^-5
tabla = [] 

# bisección para cada intervalo
for intervalo in intervalos:
    a, b = intervalo
    paso = b-a
    i = 1
    min_iteraciones = iteraciones(a, b, potenciaDeDiez)
    print(f"------------------------------------------------\nNúmero mínimo de iteraciones para el intervalo [{a}, {b}]\ny la ecuación: {min_iteraciones}")
    print(f"------------------------------------------------\nIntervalo: [{a}, {b}]")
    while (paso >= potenciaDeDiez):
        c = (a+b)/2
        fc = funcionx(c)
        fa = funcionx(a)
        fac = funcionx(a) * funcionx(c)
        tabla.append([i,a,b,c,fc,fac])
        i = i+1
        cambia = np.sign(fa) * np.sign(fc)
        if (cambia < 0):
            b = c
        else:
            a = c
        paso = b-a

    # PRINT TABLA
    if np.sign(fa) * np.sign(funcionx(b)) < 0: # se verifica si la función cambia de signo en el intervalo
        print(f"La función converge en este intervalo.\nRaíz aproximada: {c}\n------------------------------------------------")
    else:
        print("NO CONVERGE en este intervalo (no hay raíz).\n------------------------------------------------")

# DataFrame con la tabla para guardar en Excel
df = pd.DataFrame(tabla, columns=["Iteración", "a", "b", "c", "f(c)", "f(ac)"])

# archivo Excel "el-nombre-que-sea.xlsx"
df.to_excel("resultado_biseccion5.xlsx", index=False, engine='openpyxl')
print("Nombre del archivo 'resultado_biseccion5.xlsx'") 