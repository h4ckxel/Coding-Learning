import random
import time

class Ordenamientos:
    """
    Clase que implementa diversos algoritmos de ordenamiento.
    Incluye: Burbuja, Inserción, Shell y QuickSort.
    """

    def burbuja(self, lista):
        """
        Ordena una lista utilizando el algoritmo de ordenamiento Burbuja.
        Mide y muestra el tiempo de ejecución.
        """
        inicio = time.time()
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        fin = time.time()
        print(f"Tiempo de ejecución de Burbuja: {fin - inicio:.6f} segundos")

    def insertion(self, lista):
        """
        Ordena una lista utilizando el algoritmo de ordenamiento por Inserción.
        Mide y muestra el tiempo de ejecución.
        """
        inicio = time.time()
        for i in range(1, len(lista)):
            key = lista[i]
            j = i - 1
            while j >= 0 and key < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = key
        fin = time.time()
        print(f"Tiempo de ejecución de Inserción: {fin - inicio:.6f} segundos")

    def shell(self, lista):
        """
        Ordena una lista utilizando el algoritmo de ordenamiento Shell.
        Mide y muestra el tiempo de ejecución.
        """
        inicio = time.time()
        n = len(lista)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = lista[i]
                j = i
                while j >= gap and lista[j - gap] > temp:
                    lista[j] = lista[j - gap]
                    j -= gap
                lista[j] = temp
            gap //= 2
        fin = time.time()
        print(f"Tiempo de ejecución de Shell: {fin - inicio:.6f} segundos")

    def quicksort(self, lista, inicio, fin):
        """
        Ordena una lista utilizando el algoritmo de ordenamiento QuickSort.
        Mide y muestra el tiempo de ejecución.
        """
        if inicio < fin:
            pivote_index = self.partition(lista, inicio, fin)
            self.quicksort(lista, inicio, pivote_index - 1)
            self.quicksort(lista, pivote_index + 1, fin)

    def partition(self, lista, inicio, fin):
        """
        Función auxiliar para el algoritmo QuickSort.
        Encuentra el pivote y organiza la lista en torno a él.
        """
        pivote = lista[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            if lista[j] <= pivote:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
        return i + 1

    def ordenar(self, lista, algoritmo):
        """
        Ordena una lista utilizando el algoritmo seleccionado por el usuario.
        1: Burbuja, 2: Inserción, 3: Shell, 4: QuickSort.
        Muestra el tiempo de ejecución y el estado de la lista antes y después de ordenar.
        """
        print(f"Lista original: {lista}")
        inicio = time.time()

        if algoritmo == 1:
            self.burbuja(lista)
        elif algoritmo == 2:
            self.insertion(lista)
        elif algoritmo == 3:
            self.shell(lista)
        elif algoritmo == 4:
            self.quicksort(lista, 0, len(lista) - 1)
            fin = time.time()
            print(f"Tiempo de ejecución de QuickSort: {fin - inicio:.6f} segundos")

        print(f"Lista ordenada: {lista}")

def main():
    """
    Función principal que realiza la demostración de la clase Ordenamientos.
    Genera una lista aleatoria y solicita al usuario seleccionar un algoritmo.
    """
    # Solicita al usuario el número de elementos de la lista
    num_elementos = int(input("Ingresa el número de elementos para la lista a ordenar: "))
    lista = [random.randint(0, 1000) for _ in range(num_elementos)]

    # Muestra los algoritmos disponibles
    print("Selecciona el algoritmo de ordenamiento que deseas utilizar:")
    print("1. Burbuja")
    print("2. Inserción")
    print("3. Shell")
    print("4. QuickSort")

    # Solicita la elección del algoritmo
    seleccion = int(input("Introduce el número correspondiente al algoritmo de ordenamiento: "))

    # Crea una instancia de la clase Ordenamientos
    ordenamientos = Ordenamientos()
    ordenamientos.ordenar(lista, seleccion)

if __name__ == "__main__":
    main()
