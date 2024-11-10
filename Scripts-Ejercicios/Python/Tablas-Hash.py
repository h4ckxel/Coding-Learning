class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # Calcula el índice usando la función hash y el tamaño de la tabla
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Verifica si la clave ya existe para actualizar el valor
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        # Si la clave no existe, agrega la pareja (clave, valor)
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        # Busca la clave en la lista del índice
        for item in self.table[index]:
            if item[0] == key:
                return item[1]  # Retorna el valor si encuentra la clave
        return None  # Retorna None si la clave no existe

    def delete(self, key):
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]  # Elimina la clave y el valor
                return True
        return False  # Retorna False si la clave no se encuentra

    def display(self):
        # Muestra el contenido de la tabla hash
        for i, items in enumerate(self.table):
            print(f"Índice {i}: {items}")


# Ejemplo de uso
hash_table = HashTable(10)
hash_table.insert("a", 1)
hash_table.insert("b", 2)
hash_table.insert("c", 3)
hash_table.insert("a", 4)  # Actualiza el valor de "a"
hash_table.insert("z", 5)  # Colisión con otra clave

print("Tabla Hash después de las inserciones:")
hash_table.display()

print("\nBuscar el valor asociado a la clave 'a':", hash_table.search("a"))
print("Eliminar la clave 'b':", hash_table.delete("b"))

print("\nTabla Hash después de la eliminación:")
hash_table.display()
