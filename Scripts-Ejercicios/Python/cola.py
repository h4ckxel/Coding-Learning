class Cola:
    def __init__ (self):
        self.items = []
    def is_empty(self): # is_empty verifica si la cola esta vacia
        return len(self.items) == 0
    def encolar(self, item): # agrega un item al final de la cola
        self.items.append(item)
    def desencolar (self): # elimina el item forntal de la cola
        if self.is_empty():
            raise IndexError("Cola vacía")
        return self.items.pop(0)
    def peek(self): # obtiene el item de enfrente de la cola
        if self.is_empty():
            raise IndexError("Cola vacia")
        return self.items[0]

# ejemplo de uso
cola = Cola()
print(cola.is_empty())
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print(cola.peek())
print(f"Desencolar: {cola.peek()}")
print(cola.desencolar())
print(cola.peek())
print("Encolando: 4")
cola.encolar(4)
print(f"Imprimiendo la cola: \n{cola.items}")