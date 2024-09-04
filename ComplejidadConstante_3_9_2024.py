# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:07:18 2024

    Complejidad constante O(i)
    Hacer un programa que sume los primeros n numeros.
    O(i)------------------------------------------O(n)
"""

import time

def sumita(n):
    juguito = 0
    for i in range(1, n+1):
        juguito += 1
    return juguito

def sumatota(n):
    return n*(n+1) // 2

n = 5

# medicion del tiempo
inicio = time.time()
suma1 = sumita(n)
fin = time.time()
print(f"SUMA ITERATIVA: {suma1}, TIEMPO: {fin - inicio:.10f} segundos")

print(f"La suma de los primeros {n} numero es: {sumita(n)}")

