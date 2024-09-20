# Ordenamiento por inserción
`19 / Septiembre / 2024`

### Descripción del algoritmo de inserción:

El ordenamiento por inserción funciona de manera similar a cómo ordenarías cartas en tu mano. Divide la lista en dos partes:
- Una parte ordenada (al principio de la lista)
- Una parte no ordenada (el resto de la lista)
Cada elemento de la parte no ordenada se inserta en la posición correcta de la parte ordenada.

---

## Pseudocódigo
```pseint
Insertion_sort(arreglo):
    n <-- Tamaño arreglo
    para i desde 1 hasta n-1
        key <-- arreglo[i]
        j <-- i - 1
        mientras j >= 0 y arreglo[j] > key:
            arreglo[j+1] = arreglo[j]
            j = j - 1
        FIN MIENTRAS
        arreglo[j+1] = key
    FIN PARA
FIN
```
---
## Código en Python
```python
def insertion_sort(arreglo):
    n = len(arreglo)
    for i in range(1, n):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and arreglo[j] > clave:
            arreglo[j+1] = arreglo[j]
            j -= 1
        arreglo[j+1] = clave
    return arreglo
```
---
***Documentación oficial sobre `sort` en la página de Python***: https://docs.python.org/es/3/howto/sorting.html