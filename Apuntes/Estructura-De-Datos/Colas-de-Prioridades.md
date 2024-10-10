# Colas de Prioridades

> Es una estructura similar a una cola regular, pero cada elemento tiene una prioridad asociada
> Los elementos con mayor prioridad, se atienden antes que los elementos con menor prioridad.

Si dos elementos tienen la misma prioridad: se atienden de acuerdo a su hora de llegada.

Operaciones:
- Encolar.
- Desencolar.
- Consulta de prioridad -> puede o no ser una implementación.
  
### Prioridad ---> Escala

#### Implementancion
- Usando listas enlazadad (cola de colas, listas):
> Esta idea se puede mantener una lista ordenada al insertar elementos en la posicion correcta segun su prioridad.
- Usando monticulos (heaps)
> heap -> estructura de datos jerarquica
- Usando arrays simple
  - Costosa ------------ O(n)

### Tipos de colas de prioridad
1. Colas de prioridad minima
   - Elementos de prioridad baja, se eliminan primero.
2. Colas de prioridad maxima
   - Elementos de prioridad mayor, se eliminan primero.
### Aplicaciones
- Algoritmos de busqueda de rutas. Dijkstra -> Ayuda a seleccionar el nodo mas cercano.
Metadudisticas
- Sistemas de planificacion de procesos
En Sistemas operativos:
    - Se asigna mayor prioridad a procesos criticos.
- Simulacion de eventos
  - Se usa una cola de prioridades para determinar cual evento debe procesarse primero.

---

### Problemas tipicos y  algoritmos asociados

Dijkstra: selecciona un nodo con la distancia minima, optmizando la busqueda de rutas en grafo pondrados.

Analisis de expresiones matematicas: Una pila es util para evaluar expresiones matematicas en notacion posfija (Reverse Polish Notation)

Simulacion de colas de espera: Usar colas para modelar el comportamiento de un sistema de multiples clientes.

### Ejemplo: A partir del ejemple del consultorio, agregar:

- [x] LOS PACIENTES INGRESAN A UNA COLA DE PRIORIDAD SEGUN LA GRAVEDAD DE SUS SINTOMAS

- [x] LOS PACIENTES MAS GRAVES SERAN ATENDIDOS PRIMERO TRIAGE

> [!NOTE]
> Usar gravedad = int entre 1 y 10 donde 1 es mas grave y 10 menos grave


















