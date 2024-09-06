"""
hacer un programa que divida una lista en mitades y que cuente los elementos.
 Este algoritmo divide recursivamente una lista en mitades y en cada division cuenta los elementos de la lista. 
 La recursion sigue diviendo hasta que las listas sean los suficientemente pequeñas (tamaño 1) 
 y en cada paso se realiza un cuenta lineal de los elementos ****COMPRESION DE LISTAS****
"""

import time

def contar_elementos(lista):
    if len(lista) == 1:
        return 1
    
    # Se partea la mitad la lista
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    # Cuenta los elementos de la lista
    conteo_total = len(lista)
    conteo_izquierda = contar_elementos(izquierda)
    conteo_derecha = contar_elementos(derecha)
    # Suma los conteos de la division
    return conteo_total + conteo_izquierda + conteo_derecha

# Compresion de listas
lista = [i for i in range(1, 101)]
print(lista)
print("|-------------------------------------------------|")
print(f"| Total de elementos en la lista: {len(lista)}             |")
print("|-------------------------------------------------|")

# Llama el conteo
conteo_final = contar_elementos(lista)
print(f"| Conteo total de elementos en cada paso: {conteo_final}     |")
print("|-------------------------------------------------|")

# Medidor de tiempo
inicio = time.time()
fin = time.time()

print(f"| Tiempo de ejecución: {fin - inicio:.10f} segundos      |")
print("|-------------------------------------------------|")
