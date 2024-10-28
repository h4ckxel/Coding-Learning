import csv

class Usuario:
    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo

class NodoAVL:
    def __init__(self, usuario):
        self.usuario = usuario
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, raiz, usuario):
        if raiz is None:
            return NodoAVL(usuario)
        
        # Prevención de duplicados
        if usuario.id_usuario == raiz.usuario.id_usuario:
            print("Usuario con este ID ya existe.")
            return raiz

        if usuario.id_usuario < raiz.usuario.id_usuario:
            raiz.izquierdo = self.insertar(raiz.izquierdo, usuario)
        else:
            raiz.derecho = self.insertar(raiz.derecho, usuario)
        
        # Actualizar la altura y balancear el árbol
        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierdo), self.obtener_altura(raiz.derecho))
        balance = self.obtener_balance(raiz)
        
        # Rotaciones para balanceo
        if balance > 1 and usuario.id_usuario < raiz.izquierdo.usuario.id_usuario:
            return self.rotacion_derecha(raiz)
        if balance < -1 and usuario.id_usuario > raiz.derecho.usuario.id_usuario:
            return self.rotacion_izquierda(raiz)
        if balance > 1 and usuario.id_usuario > raiz.izquierdo.usuario.id_usuario:
            raiz.izquierdo = self.rotacion_izquierda(raiz.izquierdo)
            return self.rotacion_derecha(raiz)
        if balance < -1 and usuario.id_usuario < raiz.derecho.usuario.id_usuario:
            raiz.derecho = self.rotacion_derecha(raiz.derecho)
            return self.rotacion_izquierda(raiz)
        
        return raiz

    def obtener_altura(self, nodo):
        return nodo.altura if nodo else 0

    def obtener_balance(self, nodo):
        return self.obtener_altura(nodo.izquierdo) - self.obtener_altura(nodo.derecho) if nodo else 0

    def rotacion_izquierda(self, z):
        y = z.derecho
        T2 = y.izquierdo
        y.izquierdo = z
        z.derecho = T2
        z.altura = 1 + max(self.obtener_altura(z.izquierdo), self.obtener_altura(z.derecho))
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))
        return y

    def rotacion_derecha(self, z):
        y = z.izquierdo
        T3 = y.derecho
        y.derecho = z
        z.izquierdo = T3
        z.altura = 1 + max(self.obtener_altura(z.izquierdo), self.obtener_altura(z.derecho))
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))
        return y

    def preorden(self, raiz):
        if raiz:
            print(f"ID: {raiz.usuario.id_usuario}, Nombre: {raiz.usuario.nombre}, Correo: {raiz.usuario.correo}")
            self.preorden(raiz.izquierdo)
            self.preorden(raiz.derecho)

    def guardar_datos(self, raiz, archivo):
        if raiz:
            archivo.writerow([raiz.usuario.id_usuario, raiz.usuario.nombre, raiz.usuario.correo])
            self.guardar_datos(raiz.izquierdo, archivo)
            self.guardar_datos(raiz.derecho, archivo)

    def cargar_datos(self, archivo):
        with open(archivo, mode="r", newline="") as file:
            lector = csv.reader(file)
            for fila in lector:
                if fila:
                    id_usuario = int(fila[0])
                    nombre = fila[1]
                    correo = fila[2]
                    usuario = Usuario(id_usuario, nombre, correo)
                    self.raiz = self.insertar(self.raiz, usuario)

def guardar_datos(arbol, archivo="usuarios.csv"):
    with open(archivo, mode="w", newline="") as file:
        escritor = csv.writer(file)
        arbol.guardar_datos(arbol.raiz, escritor)

def cargar_datos(arbol, archivo="usuarios.csv"):
    try:
        arbol.cargar_datos(archivo)
    except FileNotFoundError:
        print("No se encontró el archivo de datos, iniciando con árbol vacío.")

if __name__ == "__main__":
    arbol = ArbolAVL()
    cargar_datos(arbol)  # Cargar datos al inicio

    while True:
        print("\n=== Menú de Opciones ===")
        print("1. Insertar Usuario")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
        print("4. Mostrar Usuarios (Preorden)")
        print("5. Salir")
        
        opc = input("Seleccione una opción: ")
        
        if opc == "1":
            print("\n--- Insertar Usuario ---")
            id_usuario = int(input("Ingrese el ID del usuario nuevo: "))
            nombre = input(f"Ingrese el nombre del usuario {id_usuario}: ")
            correo = input(f"Ingrese el correo del usuario {id_usuario}: ")
            usuario = Usuario(id_usuario, nombre, correo)
            arbol.raiz = arbol.insertar(arbol.raiz, usuario)
            print(f"Usuario {id_usuario} insertado correctamente.")
        
        elif opc == "2":
            print("\n--- Buscar Usuario ---")
            id_usuario = int(input("Ingrese el ID del usuario a buscar: "))
            nodo_encontrado = arbol.buscar(arbol.raiz, id_usuario)
            if nodo_encontrado:
                usuario = nodo_encontrado.usuario
                print(f"Usuario encontrado: ID {usuario.id_usuario}; Nombre: {usuario.nombre}; Correo: {usuario.correo}")
            else:
                print("Usuario no encontrado")
        
        elif opc == "4":
            print("\n--- Mostrar Usuarios (Preorden) ---")
            arbol.preorden(arbol.raiz)
        
        elif opc == "5":
            print("\n--- Saliendo y Guardando Datos ---")
            guardar_datos(arbol)  # Guardar datos al salir
            print("Datos guardados exitosamente.")
            break
