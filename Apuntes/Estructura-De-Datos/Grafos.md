
<div align="center">

# GRAFOS

###### `22/24 de Octubre del 2024` 

</div>

Un grafo es una estructura de datos utilizada para representar relaciones entre objetos. Por ejemplo:

* Redes
* Algoritmos de búsqueda
* Análisis de redes sociales
* Sistemas de recomendación, etc.

### Definición formal
Un grafo es define como un par (V, E) donde 

V: un conjunto de vertices o nodos
E: un conjunto de aristas o arcos que conectan vertices

### Los aristas pueden ser

- No dirigidos: Representan una relación bidireccional entre dos nodos
- Dirigidos: Representan una relación unidireccional entre nodos

### Aplicaciones de los grafos

1. Redes Sociales
    - Modelado de relación entre usuarios
    - Análisis de comunidades y propagación de la información

2. Sistemas de recomendación
    - Modelado de relación entre usuarios
    - Descubrimiento de similitudes y recomendaciones basadas en conexión

3. Rutas y Mapas
   - Planificación de rutas optimas
   - Sistemas de navegación

4. Análisis de Redes
   - Detección de botella en redes de comunicación

5. Compiladores
   - Grafos de dependencia para optimizar el orden de la ejecución
   - Prioridad de tareas

### Tipos de grafos
Según la naturaleza de sus aristas

#### Grafos no dirigidos
  - Las aristas no tienen dirección
  - Si existe una arista entre los nodos U y V se puede ir de U ---> V y viceversa U <--- V

### Grafos dirigidos
  - Las aristas tienen dirección
  - Una arista U ---> V pero no necesariamente V ---> U

<div align="center">

<img src="https://www.researchgate.net/publication/309278789/figure/fig7/AS:750920426078218@1556044789424/Ejemplos-de-un-grafo-dirigido-y-un-grafo-no-dirigido.ppm" width="70%"/>

##### `Ejemplo de grafos`

</div>

### Tipo de Grafo según su ponderación de las aristas

 1. Grafos no ponderados
      - Todas las aristas tienen el mismo peso o costo
      - Usados cuando solo interesa la conexión, no el costo asociado
 2. Grafos ponderados
      - Los aristas tienen un peso o costo asociado
      - Utilizados para representar distancias, tiempos, costos, etc. por ejemplo: **mapas de carreteras**

### Representaciones de Grafos

1. Matriz de adjacency
2. Lista de adjacency

#### Matriz de adjacency

- Es una matriz bidimensional de $n_xn$ donde $n$ es el número de vertices.
- Cada posición $A(i)(j)$ indica la presencia (y posiblemente el peso) de una arista entre los nodos $i$ y $j$

#### Ventajas

- Acceso rápido para verificar la existencia de una arista entre dos nodos.
- Sencillez en implementar.

#### Desventajas

- Ocupa mucho espacio: $O(n²)$


### Lista de adjacency

- Para cada nodo, se mantiene una lista de sus nodos adyacentes.
- Más eficiente en términos de espacio para grafos dispersos

#### Ventajas

- Ocupa menos espacios: $O(n+m)$. Donde $m = aristas$

#### Desventajas

- Acceso más lento para verificar la existencia.

## Recorridos en Grafos

1. Búsqueda en anchura. ***Breadth-First search, BFS***
   - Explora el grafo nivel por nivel
   - Utiliza una cola para mantener el orden de visita
   - Es util para encontrar la distancia minima (***numero de aristas***) desde el nodo inicial a los demás nodos en grafos no ponderados

### Algoritmo:

1. Iniciar desde un nodo fuente y marcarlo como visitado
2. Agregar el nodo a una cola
3. Mientras la cola no este vacía:
   - Extraer el nodo frontal de la cola
   - Para cada nodo adyacente no visitado:
      - Marcarlo como visitado
      - Agregarlo a la cola

## Pseudocódigo

```Pseint
BFS(Grafo G, Nodo S)
   Crear cola Q
   Marcar S como visitado
   Q.encolar(S)
   Mientras Q no vacía:
      u=Q.desencolar()
      Para cada nodo V
         adyacente a u
         Si v no ha sido visitado
            marcar v como visitado
            Q.encolar(u)
```

$G(V), E={}$

$v=6$

$E{
   (0,1)
   (0,2)
   (1,2)
   (2,0)
   (2,3)
   (3,3)
   (3,4)
   (4,3)
}$

## Recorrido DFS
Búsqueda en profundidad

El algoritmo explora un grafo tan profundo como sea posible antes de retroceder.

Utiliza una pila para mantener el orden de los nodos por visitar.

DFS: ***Deep First Search***

- Detección ciclos en los grafos
- Resolución de laberintos

$O(V+E)$

#### Algoritmo
1. Se elige el nodo inicial y se marca como visitado
2. Recursion: Para cada nodo adyacente no visitado se llama recursivamente a la función **DFS**
3. Retroceso: Cuando no quedan nodos adyacentes sin visitor, se retrocede al nodo anterior
4. Repetición: Este proceso continua hasta que se hayan visitado todos los nodos alcanzables desde el nodo inicial.
5. Componentes desconectados
   - Si existen nodos no visitados después de completar el **DFS** desde el nodo inicial, se repite el proceso desde uno de esos nodos.












