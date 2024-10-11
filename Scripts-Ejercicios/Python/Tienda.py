# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 22:55:36 2024

@author: Acxel
"""

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = Pila()
        self.siguiente = None

class Cola:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def encolar(self, cliente):
        self.items.append(cliente)
    
    def desencolar(self):
        # elimina al cliente que está al frente de la cola
        if self.is_empty():
            raise IndexError("\nCola vacía. No hay cliente por atender.")
        return self.items.pop(0)
    
    def peek(self):
        # obtiene el cliente al frente de la cola sin eliminarlo
        if self.is_empty():
            raise IndexError("\nCola vacía. No hay clientes en espera.")
        return self.items[0]

    def size(self):
        # muestra todos los clientes que están en la cola
        if self.is_empty():
            print("\nNo hay clientes en espera.")
        else:
            print("\nClientes en espera:")
            for cliente in self.items:
                print(f"Cliente: {cliente.nombre}")

class Pila:
    def __init__(self):
        self.superior = None
    
    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo
        print(f"Agregando {dato} a la pila de productos.")
    
    def pop(self):
        if self.superior is None:
            print("La pila de productos está vacía.")
            return None
        dato = self.superior.dato
        self.superior = self.superior.siguiente
        return dato
    
    def is_empty(self):
        return self.superior is None
    
    def size(self):
        contador = 0
        nodo_actual = self.superior
        while nodo_actual:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def main():
    fila = Cola()
    
    while True:
        print("\n1. Agregar cliente")
        print("2. Atender al siguiente cliente")
        print("3. Ver siguiente cliente")
        print("4. Salir del programa")
        
        try:
            opc = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("\nPor favor, ingrese un número válido.")
            continue
        
        if opc == 1:
            nombre = input("\nNombre del cliente: ")
            cliente = Cliente(nombre)
            while True:
                producto = input(f"Ingrese un producto para {nombre} (o escriba 'fin' para terminar): ")
                if producto.lower() == 'fin': # utlizo .lower() para que el usuario pueda teclear FIN, Fin, fin, etc.
                    break
                cliente.productos.push(producto)
            fila.encolar(cliente)
        
        elif opc == 2:
            if fila.is_empty():
                print("\nNo hay clientes para atender.")
            else:
                cliente = fila.desencolar()
                print(f"\nAtendiendo al cliente: {cliente.nombre}")
                while not cliente.productos.is_empty():
                    producto = cliente.productos.pop()
                    print(f"Procesando producto: {producto}")
                print(f"Todos los productos de {cliente.nombre} han sido procesados.")
        
        elif opc == 3:
            if fila.is_empty():
                print("\nNo hay clientes en espera.")
            else:
                cliente = fila.peek()
                print(f"\nEl siguiente cliente en la cola es: {cliente.nombre}")
        
        elif opc == 4:
            print("\nSaliendo del programa...")
            break
        
        else:
            print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
