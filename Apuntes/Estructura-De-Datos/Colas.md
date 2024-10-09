# Colas (***Queue***) 
###### `9 de Octubre del 2024`

Es un TDA que sigue la idea politica/principio de "***First In, First Out***"

El primer elemento de la cola se le conoce como "***frontal***"

El ultimo se le conoce como trasero.

`[1, 2, 3, 5, 7] ---> 1 = frontal, 7 = trasero`

`Agregar un elemento -> encolar, poner en cola (***en queue***)`

Analogia: es como una persona se ponga en una fila.

El elemento agregado siempre será el elemento trasero.

Eliminar un elemento de la cola se le conoce como "***dequeue***" -> Eliminar/Borrar el frontal (el que esta al inicio)

> [!NOTE]
> solo se puede eliminar el frontal

#### Implementación
1. Definimos una clase cola.
2. Definimos una lista vacia, que almacenará los elementos de la lista.
3. Inicializar dos variables "***delantero***" y "***trasero***".
4. Inicializar con *-1* para mostrar que la lista este vacia.

```Python
class Cola:
    def __init__ (self):
        self.items = []
    def is_empty(self): # is_empty verifica si la cola esta vacia
        return len(self.items) == 0
    def encolar(self, item): # agrega un item al final de la cola
        self.items.append(item)
    def desencolar (self): # elimina el item forntal de la cola
        if is_empty():
            rase IndexError("Cola vacía")
        return self.items.pop(0)
    def peek(self): # obtiene el item de enfrente de la cola
        if is_empty():
            rase IndexError("Cola vacia")
        return self.items(0)
```