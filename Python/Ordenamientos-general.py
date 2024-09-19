import random
import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_aort import insertion_sort as injerto

huarache = [random.randint(1, 1000) for _ in range(10000)]

# ordenamiento burbuja
inicio = time.time()
bubble_sort(huarache)
fin = time.time()
print(f"\nOrdenamiento por Burbuja. Tiempo: {fin - inicio: .10f} segundos")

# ordenamiento selection sort
inicio = time.time()
selection_sort(huarache)
fin = time.time()
print(f"\nOrdenamiento por Selection Sort. Tiempo: {fin - inicio: .10f} segundos")

# ordenamiento burbuja
inicio = time.time()
sorted(huarache)
fin = time.time()
print(f"\nOrdenamiento por Sorted(Python). Tiempo: {fin - inicio: .10f} segundos")

# ordenamiento burbuja
inicio = time.time()
injerto(huarache)
fin = time.time()
print(f"\nOrdenamiento por Sorted(Python). Tiempo: {fin - inicio: .10f} segundos")
