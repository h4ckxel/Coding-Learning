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
