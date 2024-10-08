# clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# hacer nuevos nodos va a proveer las operaciones de pilas
class Pila:
    def __init__(self, dato):
        self.superior = None
    
    def push(self, dato):
        print(f"Agregando {dato} a la cima de la pila") # si no hay datos agregamos el valor en el elemento superior
        if self.superior == None:
            self.superior = Nodo(dato)
            return 0
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo
