# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:07:18 2024

    Complejidad constante O(i)
    Hacer un programa que sume los primeros n numeros.
    O(i)------------------------------------------O(n)
"""

import time

def suma(n):
    zuma = 0
    for i in range(1, n+1):
        zuma += 1
    return zuma

def bigsuma(n):
    return n*(n+1) // 2

n = 5

# medicion del tiempo
inicio = time.time()
suma1 = suma(n)
fin = time.time()
print(f"SUMA ITERATIVA: {suma1}, TIEMPO: {fin - inicio:.10f} segundos")

print(f"La suma de los primeros {n} numero es: {suma(n)}")

