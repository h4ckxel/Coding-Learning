<div align="center">

# Tablas Hash

### `Noviembre 6, 2024`

</div>

---


Las **tablas hash** son una estructura de datos que permite almacenar y recuperar elementos de forma rápida mediante una clave única para cada valor. Esto se logra usando una **función hash** que convierte la clave en un índice donde se almacena el valor en un array.

## ¿Qué es una Tabla Hash?

Una tabla hash consiste en:

1. **Array**: Contiene las ubicaciones (índices) donde se almacenarán los valores.
2. **Función Hash**: Convierte la clave en un índice.
3. **Manejo de Colisiones**: Método para resolver conflictos cuando varias claves se convierten en el mismo índice.

**Ventajas**:
- **Búsqueda rápida**: Recuperación en tiempo constante promedio \(O(1)\).
- **Inserción y eliminación rápida**: También de complejidad promedio \(O(1)\).

**Desventajas**:
- Puede volverse ineficiente con muchas colisiones.
- Requiere diseño cuidadoso para la función hash y manejo de colisiones.

---

## ¿Qué es una Función Hash?

La **función hash** convierte una clave de entrada en un número entero (el índice del array). Debe cumplir ciertas propiedades para ser efectiva:

1. **Determinista**: La misma entrada siempre debe producir el mismo índice.
2. **Distribución Uniforme**: Debe distribuir los índices de manera uniforme para evitar colisiones.
3. **Eficiencia**: Debe ser rápida de calcular.

Ejemplo en pseudocódigo:
```python
def simple_hash(key):
    hash_value = 0
    for char in key:
        hash_value += ord(char)
    return hash_value % size_of_table
```

En este ejemplo, `ord(char)` convierte cada carácter en un número y luego calcula el módulo con el tamaño de la tabla para determinar el índice.

### Ejemplo Visual de Función Hash

![Función Hash](https://i.imgur.com/6Sk6UwO.png)
> *La función hash convierte una clave en un índice de la tabla.*

---

## Manejo de Colisiones

Las **colisiones** ocurren cuando dos claves diferentes producen el mismo índice. Para manejar esto, existen varias técnicas:

### 1. Encadenamiento (Chaining)

Cada índice de la tabla almacena una lista de elementos. Si ocurre una colisión, el elemento se añade a la lista en ese índice.

- **Ventaja**: No es necesario redimensionar la tabla.
- **Desventaja**: Puede degradar el rendimiento con muchas colisiones.

```python
hash_table = [[] for _ in range(size)]
def insert(hash_table, key, value):
    index = hash_function(key)
    hash_table[index].append((key, value))
```

![Encadenamiento](https://i.imgur.com/TZmJYKO.png)
> *Ejemplo de manejo de colisiones con encadenamiento.*

### 2. Direccionamiento Abierto (Open Addressing)

En lugar de almacenar una lista, se busca el siguiente índice disponible. Existen varios métodos de direccionamiento abierto:

- **Lineal**: Busca el siguiente índice secuencialmente.
  - $h_i(k) = (h(k)+i)mod m$
- **Cuadrático**: Utiliza una fórmula cuadrática para los saltos.
  - $h_i(k) = (h(k)+C_3 i+C_2 i²)mod m$
- **Doble Hashing**: Usa una segunda función hash para determinar el salto.
  - $h_i(k) = (h(k)+ i*h_2(k))mod m$

#### Ventajas

- Utiliza menos memoria

#### Desventajas

- El rendimiento baja con una alta carga de factores

---

## Implementación Básica en Python

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None
```

---

## Consideraciones para Diseñar una Función Hash

Para diseñar una buena función hash:

1. **Distribuir uniformemente**: Evitar grupos de índices con muchas colisiones.
2. **Mantener baja complejidad**: Debe ser rápida y eficiente para grandes volúmenes de datos.
3. **Evitar claves similares**: Evitar patrones que generen colisiones frecuentes.

**Ejemplo de una función hash mejorada para cadenas largas:**
```python
def better_hash(key):
    hash_value = 5381
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value % size_of_table
```

---

## Ejemplo Completo de Uso

Supongamos que tenemos una lista de personas y queremos almacenar sus números de teléfono en una tabla hash.

```python
hash_table = HashTable(10)
hash_table.insert("Alice", "123-4567")
hash_table.insert("Bob", "987-6543")
hash_table.insert("Charlie", "555-0000")

print(hash_table.get("Alice"))   # Output: "123-4567"
print(hash_table.get("Bob"))     # Output: "987-6543"
print(hash_table.get("Charlie")) # Output: "555-0000"
```

## Aplicaciones de las Tablas Hash

Las tablas hash son útiles en varios escenarios:
- **Bases de datos**: Para índices de acceso rápido.
- **Caches**: Almacenamiento temporal de datos para accesos rápidos.
- **Sistemas de archivos**: Almacenamiento de rutas y archivos.


## Colisión

Aquel evento donde dos valores van a dar a un mismo indice.

## Resolución de Colisiones

1. Encadenamiento separado (Separate Chaining)
2. Direccionamiento Abierto (Open Addressing)

## Encadenamiento separado

<div align="center">

<img src="https://i.sstatic.net/9aLZB.png" width="70%">

solución: hace una lista encadenada en el arreglo hash

</div>

El arreglo se ha transformado en un arreglo de la lista encadenada donde cada casilla apunta a una lista encadenado


>>>[!NOTE]
Un array solo acepta un solo tipo de dato, en cambio las listas aceptan cualquier tipo de dato
Index es un tipo de apuntador

Ventajas:

- Fácil implementación

Desventajas:

- Puede consumir más memoria
- El rendimiento puede degradarse si las listas se vuelven largas



---

## Conclusión

Las tablas hash son una estructura fundamental en informática, ideal para problemas donde se requiere acceso rápido. Un diseño adecuado de la función hash y una buena estrategia de manejo de colisiones son claves para su eficiencia.

--- 

#### Compresión de archivos