def insertion_sort(arreglo):
    n = len(arreglo)
    for i in range(1, n-1):
        clave = arreglo[i]
        j = i - 1
        while j >= 0 and arreglo[j] > clave:
            arreglo[j+1] = arreglo[j]
            j -= 1
        arreglo[j+1] = clave
    return arreglo