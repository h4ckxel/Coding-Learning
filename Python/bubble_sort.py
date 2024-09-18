# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:44:30 2024

@author: h4ckxel
"""


def bubble_sort(arreglo):
    n = len(arreglo)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo [j+1]:
                #arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                aux = arreglo [j]
                arreglo[j] = aux
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = aux
        #     print(f"Paso: {j+1}")
        #     print(f"Se intercambia {arreglo[j]} por  {arreglo[j+1]}")
        #     print(arreglo)
        # print()
    return arreglo
    
# # arreglo ejemplo
# huarache = [7,3,9,11,1,0,8]
# print("Arreglo original: ", huarache)

# # ordenar arreglo
# bubble_sort(huarache)
# print("Arreglo ordenado es: ", huarache)
