# Selection Sort 

``` 18 / Septiembre / 2024 ```

- Funciona dividiendo el arreglo en dos partes:
    - Una parte ordenada
    - Una parte no ordenada
- En cada iteracion el elemento minimo de la parte no ordenada se selecciona y se intercambia con el primer elemento de la parte no ordenada. 
  
  ```pseint
    Selection_sort(arreglo):
        n <--- Tamaño arreglo
        para i desde 0 hasta n-1
            min_index <-- i # Suponer que el minimo esta en el indice i
            para j desde i + 1 hasta n - 1 - i hacer:
                SI arreglo[j] < arreglo[min_index] entonces:
                    min_index = j
                FIN SI 
            SI min_index != i entonces:
                intercambiar arreglo[i] y arreglo[min_index]
            FIN SI
        FIN PARA RETURN ARREGLO
    FIN
  ```

  #### Código en Python

  ```python
  def selection_sort(arreglo):
    n = len(arreglo)
    for i in range(n):
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
