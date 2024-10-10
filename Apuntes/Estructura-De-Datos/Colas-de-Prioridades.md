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