# -*- coding: utf-8 -*-
"""
hacer un programa que divida una lista en mitades y que cuente los elementos.
 Este algoritmo divide recursivamente una lista en mitades y en cada division cuenta los elementos de la lista. 
 La recursion sigue diviendo hasta que las listas sean los suficientemente pequeñas (tamaño 1) 
 y en cada paso se realiza un cuenta lineal de los elementos ****COMPRESION DE LISTAS****
"""

lista = [i for i in range(1, 101)]
print("--------------------------------------------------")
print(f"Lista completa: {lista}")
print(f"Tamaño de lista: {len(lista)}")

mitad = int(len(lista)/2)
print("La mitad de la lista es: ", mitad)
print("--------------------------------------------------")

izquierda = lista[:mitad]
derecha = lista[mitad:]

print("Lista izquierda: ", izquierda)
print(f"Tamaño de lista izquierda {len(izquierda)}")
print("--------------------------------------------------")
print("Lista derecha: ", derecha)
print(f"Tamaño de lista derecha: {len(derecha)}")
print("--------------------------------------------------")
