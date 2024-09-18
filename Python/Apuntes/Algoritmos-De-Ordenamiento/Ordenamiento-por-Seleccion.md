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