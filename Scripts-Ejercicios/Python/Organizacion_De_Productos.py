class Producto:
    def __init__(self, nombre = str, precio = float):
        self.nombre = nombre
        self.precio = precio

# Funcion para ordenar por precio
def ordenarPrecio(productos = list):
    n = len(productos)
    for i in range(n):
        for j in range(0, n-i-1):
            if productos[j].precio > productos[j+1].precio:
                #arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                productos[j], productos[j+1] = productos[j+1], productos[j]

def convertir(productos = list):
    precios = []
    for producto in productos:
        producto.append(producto.precio)
    return precios
class Super:
    def printProductos(productos = list):
        for prodi in productos:
            print(f"Nombre del producto: {prodi.nombre}\nPrecio: ${prodi.precio}\n--------------------")
    def comprar(productos = list):
        costo = 0
        for producto in productos:
            costo += producto.precio
        print(f"La suma total del super es: ${costo}")
        return costo

# Base de datos
baseDeDatos = [
            Producto("Cable USB", 99.99),
            Producto("Arteck Monitor 21.5''", 1493.17),
            Producto("MousePad", 139.00),
            Producto("HyperX Mic", 969.08),
            Producto("Xtreme PC", 6899.00),
            Producto("Logitech G502", 2164.71),
            ]

# Imprimir la lista de productos
print("\nLa lista de productos es: \n")
Super.printProductos(baseDeDatos)

# imprimir lista ordenada por precio
ordenarPrecio(baseDeDatos)
print("\nLista ordenada por precio (Menor a Mayor):\n")
for producto in baseDeDatos:
    print(f"Nombre: {producto.nombre}\nPrecio: ${producto.precio}\n----------------------------------------")

#Super.comprar(baseDeDatos)
