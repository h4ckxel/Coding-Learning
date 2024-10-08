# Shell Short
`2 / Octubre / 2024`

Mejora el ordenamiento tipo inserción permie comparar y mover elementos que estan separados entre si por una brecha GAP.

### Estado Inicial
#### `[19,8,4,1,7,11,3,10,15]`

```python 
gap = int(len(arreglo) / 2) = 4
```
#### Comparar elementos de distancia 4

$19 > 17$

### Despues de comparar 19 y 17 el arreglo queda como:

#### `[7,8,4,1,19,11,2,10,15]`

## Pseudocodigo
```pseint
sellShort(arreglo):
    n <--- ongitud del arreglo
    gap <--- n/2
        # continuar hasta que gap sea 0
        mientras gap > 0 hacer
        #recorrer los elementos desde el gap hasta el final del arreglo
            Para i desde gap hasta ? hcaer
                # guardar el valor actual en varable temporal
                temp <--- arreglo[i]
                #

