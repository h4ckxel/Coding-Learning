class HashTableDB:
    def __init__(self, size):
        self.size = size
        # Inicializa la tabla hash con listas vacías para manejo de colisiones
        self.table = [[] for _ in range(size)]
        
    def _hash_function(self, key):
        # Calcula el índice a partir de la clave (ajusta la función hash según sea necesario)
        return key % self.size

    def insert(self, key, nombre, edad, ciudad):
        """
        Inserta un nuevo registro en la tabla hash.
        Args:
            key (int): Clave única del registro.
            nombre (str): Nombre del usuario.
            edad (int): Edad del usuario.
            ciudad (str): Ciudad del usuario.
        """
        index = self._hash_function(key)
        # Agrega el par (clave, [nombre, edad, ciudad]) a la lista en el índice correspondiente
        self.table[index].append((key, [nombre, edad, ciudad]))
        print(f"Registro insertado: {key} -> {nombre}, {edad}, {ciudad}")

    def update(self, key, attribute, new_value):
        """
        Actualiza un atributo específico de un registro dado su clave.
        Args:
            key (int): Clave del registro a actualizar.
            attribute (str): Atributo a modificar ("nombre", "edad", "ciudad").
            new_value: Nuevo valor para el atributo.
        """
        # 1. Calcula el índice usando la función hash
        index = self._hash_function(key)
       
        # 2. Busca el registro en la lista correspondiente al índice
        for pair in self.table[index]:
            if pair[0] == key:  # Si encuentra la clave
                # 3. Identifica y actualiza el atributo correspondiente
                if attribute == "nombre":
                    pair[1][0] = new_value  # Modifica el nombre
                elif attribute == "edad":
                    pair[1][1] = new_value  # Modifica la edad
                elif attribute == "ciudad":
                    pair[1][2] = new_value  # Modifica la ciudad
                else:
                    print("Atributo no encontrado.")  # Maneja un atributo no válido
                return  # Finaliza la función tras actualizar
       
        # 4. Si no encuentra la clave, imprime un mensaje
        print("Clave no encontrada en la tabla.")

    def search(self, key):
        """
        Busca un registro en la tabla hash usando su clave.
        Args:
            key (int): Clave del registro que se desea buscar.
        Returns:
            list: Los datos del registro si se encuentra, o un mensaje indicando que no fue encontrado.
        """
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return "Clave no encontrada en la tabla."

    def display(self):
        """
        Muestra el contenido completo de la tabla hash.
        """
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Índice {i}: {bucket}")
            else:
                print(f"Índice {i}: vacío")

# Ejemplo de uso de la tabla hash con las operaciones de inserción, actualización y búsqueda

# Crea una instancia de HashTableDB con un tamaño especificado
db_index = HashTableDB(10)

# Inserta algunos registros en la tabla hash
db_index.insert(1, "Alice", 25, "New York")
db_index.insert(2, "Bob", 30, "San Francisco")
db_index.insert(11, "Charlie", 35, "Los Angeles")  # Clave que causa colisión con la clave 1

# Muestra la tabla hash antes de la actualización
print("\nTabla Hash antes de la actualización:")
db_index.display()

# Actualiza la ciudad de "Alice" a "Boston"
db_index.update(1, "ciudad", "Boston")

# Actualiza la edad de "Bob" a 31
db_index.update(2, "edad", 31)

# Intenta actualizar un atributo que no existe
db_index.update(1, "salario", 5000)

# Muestra la tabla hash después de las actualizaciones
print("\nTabla Hash después de la actualización:")
db_index.display()

# Busca y muestra el registro actualizado de "Alice"
print("\nBúsqueda del registro de clave 1 (Alice):")
print(db_index.search(1))

# Muestra todos los registros en la tabla hash
print("\nContenido completo de la tabla hash:")
db_index.display()
