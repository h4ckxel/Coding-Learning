# Selection Sort 

``` 18 / Septiembre / 2024 ```

Las listas de Python tienen un método incorporado `list.sort()` que modifica la lista in situ. También hay una función incorporada `sorted()` que crea una nueva lista ordenada a partir de un iterable.

En este documento exploramos las distintas técnicas para ordenar datos usando `Python`.

Conceptos básicos de ordenación
Una clasificación ascendente simple es muy fácil: simplemente llame a la función `sorted()`. Retorna una nueva lista ordenada:
```python
>>>
sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
```
También puede usar el método `list.sort()`. Modifica la lista in situ (y retorna `None` para evitar confusiones). Por lo general, es menos conveniente que `sorted()`, pero si no necesita la lista original, es un poco más eficiente.
```python
>>>
a = [5, 2, 3, 1, 4]
a.sort()
a
[1, 2, 3, 4, 5]
```
Otra diferencia es que el método `list.sort()` solo aplica para las listas. En contraste, la función `sorted()` acepta cualquier iterable.

```python
>>>
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]
```
- Funciona dividiendo el arreglo en dos partes:
    - Una parte ordenada
    - Una parte no ordenada
- En cada iteracion el elemento minimo de la parte no ordenada se selecciona y se intercambia con el primer elemento de la parte no ordenada. 

---
## Pseudocódigo

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
---
  ## Código en Python

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
```
---
***Documentación oficial sobre `sort` en la página de Python: https://docs.python.org/es/3/howto/sorting.html***