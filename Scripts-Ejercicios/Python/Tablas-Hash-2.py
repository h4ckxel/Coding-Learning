class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # Calcula el índice usando el hash de la clave
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Actualiza el valor si la clave ya existe
                return
        # Si la clave no existe, agrega el par (clave, valor)
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]  # Retorna el valor asociado a la clave
        return None  # Retorna None si la clave no existe

    def delete(self, key):
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]  # Elimina el par (clave, valor)
                return True
        return False  # Retorna False si la clave no se encuentra

    def display(self):
        # Muestra el contenido de la tabla hash
        for i, items in enumerate(self.table):
            print(f"Índice {i}: {items}")


class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, size=10):
        # Crea una nueva tabla hash en la base de datos
        if table_name in self.tables:
            print(f"La tabla '{table_name}' ya existe.")
            return
        self.tables[table_name] = HashTable(size)
        print(f"Tabla '{table_name}' creada con éxito.")

    def insert_record(self, table_name, key, value):
        # Inserta un registro en la tabla especificada
        if table_name not in self.tables:
            print(f"La tabla '{table_name}' no existe.")
            return
        self.tables[table_name].insert(key, value)
        print(f"Registro ({key}: {value}) insertado en la tabla '{table_name}'.")

    def search_record(self, table_name, key):
        # Busca un registro en la tabla especificada
        if table_name not in self.tables:
            print(f"La tabla '{table_name}' no existe.")
            return None
        return self.tables[table_name].search(key)

    def delete_record(self, table_name, key):
        # Elimina un registro de la tabla especificada
        if table_name not in self.tables:
            print(f"La tabla '{table_name}' no existe.")
            return False
        result = self.tables[table_name].delete(key)
        if result:
            print(f"Registro con clave '{key}' eliminado de la tabla '{table_name}'.")
        else:
            print(f"Clave '{key}' no encontrada en la tabla '{table_name}'.")
        return result

    def display_table(self, table_name):
        # Muestra el contenido de una tabla específica
        if table_name not in self.tables:
            print(f"La tabla '{table_name}' no existe.")
            return
        print(f"Contenido de la tabla '{table_name}':")
        self.tables[table_name].display()

    def display_database(self):
        # Muestra todas las tablas y sus contenidos
        for table_name, table in self.tables.items():
            print(f"\nTabla '{table_name}':")
            table.display()


# Ejemplo de uso
db = Database()
db.create_table("Usuarios", 5)
db.insert_record("Usuarios", "Alice", {"edad": 25, "email": "alice@example.com"})
db.insert_record("Usuarios", "Bob", {"edad": 30, "email": "bob@example.com"})
db.insert_record("Usuarios", "Charlie", {"edad": 35, "email": "charlie@example.com"})

print("\nBuscar el registro de 'Alice':")
print(db.search_record("Usuarios", "Alice"))

print("\nEliminar el registro de 'Bob':")
db.delete_record("Usuarios", "Bob")

print("\nContenido de la tabla 'Usuarios':")
db.display_table("Usuarios")
