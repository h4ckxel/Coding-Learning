def selection_sort(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        # min_index = i
        min_index = i
        for j in range(i + 1, n):
            # comparacion
            if arreglo[j] < arreglo[min_index]:
                min_index = j
        # intercambio
        if min_index != i:
            aux = arreglo[i]
            arreglo[i] = arreglo[min_index]
            arreglo[min_index] = aux    
    return arreglo
