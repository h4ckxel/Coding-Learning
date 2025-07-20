# Estructuras Dinámicas lineales

###### `8 de Octubre del 2024`

- Listas
- Pilas
- Colas
- Colas de prioridades
- Aplicación de algoritmos

### TDA: Tipo de Dato Abtracto

Un conjunto de **_operaciones_** que se puede realizar sobre un conjunto de datos.

#### **Conceptos clave**

- Abstracto: Es un tipo de dato que se define por su comportamiento y no por su implementación.

En general un TDA se basa en las operaciones que soporta

1. Operaciones Constructoras. (POO) ---> Crean o inicializan un TDA
2. Operaciones de Acceso. ---> Permiten acceder o verificar datos en un TDA pero sin modificarlos.
3. Operaciones Mificadoras. ---> cambiar el estado del TDA de alguna manera. Borrar, Copiar, Eliminar.

---

## Pila (stack)

Una pila e un TDA que sigue la politica "_el último en entrar es el primero en salir_" LIFO (_Last In, First Out_)

#### Operaciones

- apilar **_push()_**: Inserta un elemento
- eliminar **_pop()_**: Elimina y retorna el elemento de la parte superior
- husmear **_peek()_**: Ver elemento de la parte de superior pero sin eliminarlo
- ¿Esta vacía? **_is_empty()_**: Verifica si la pila esta vacía

PILA ----> lista aligada

Existe un **_Nodo Superior_**

**_Nodo_**: Representa a un elemento de la pila. Este nodo tiene un dato de cualquier tipo y un apuntador a otro nodo que sera el que esta debajo de el.

`instancia = inicializar el constructor`

Cuando se crea una **_instancia_** de la pila no se deben enviar argumentos, ya que la misma pila ya inicializa con el nodo superior vacio.

---

## Ejemplo

```python
# clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# hacer nuevos nodos va a proveer las operaciones de pilas
class Pila:
    def __init__(self):
        self.superior = None

    def push(self, dato):
        print(f"Agregando {dato} a la cima de la pila") # si no hay datos agregamos el valor en el elemento superior
        if self.superior == None:
            self.superior = Nodo(dato)
            return 0
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    # si no hay datos en el nodo superior, regresamos
    def pop(self):
        if self.superior == None:
            print("La pila esta vacia")
            return 0
        print(f"Desapilar {self.superior.dato}")
        self.superior = self.superior.siguiente

    def peek(self):
        print("Imprimiendo la Pila: ")
        # se recorre la pila y se imprimen valores
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            print("")
            nodo_temporal = nodo_temporal.siguiente

# uso de la pila
pila = Pila()
pila.push("Jenny Rivera")
pila.push("El peje")
pila.push("Vladimir Putin")
pila.peek()
pila.pop()
pila.peek()
pila.push("Leon S. Kennedy")
pila.peek()
pila.pop()
pila.peek()
```

```
>>>
Agregando Jenny Rivera a la cima de la pila
Agregando El peje a la cima de la pila
Agregando Vladimir Putin a la cima de la pila
Imprimiendo la Pila:
Vladimir Putin,
El peje,
Jenny Rivera,
Desapilar Vladimir Putin
Imprimiendo la Pila:
El peje,
Jenny Rivera,
Agregando Leon S. Kennedy a la cima de la pila
Imprimiendo la Pila:
Leon S. Kennedy,
El peje,
Jenny Rivera,
Desapilar Leon S. Kennedy
Imprimiendo la Pila:
El peje,
Jenny Rivera,
```

---
