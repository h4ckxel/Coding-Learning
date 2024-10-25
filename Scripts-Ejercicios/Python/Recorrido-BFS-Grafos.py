class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adyacencia = [[] for _ in range(num_vertices)]
        
    # método para agregar una arista al grafo
    def agregar_arista(self, origen, destino):
        self.lista_adyacencia[origen].append(destino) # se agrega el destino a la lista origen
        # para grafo no dirigido:
        self.lista_adyacencia[destino].append(origen)
        
    # método para realizar BFS desde un vértice fuente
    def BFS(self, fuente):
        visitado = [False] * self.num_vertices # lista para rastrear nodos visitados
        cola = [] # cola para mantener el orden de visita
        
        visitado[fuente] = True     # se marca el nodo fuente como visitado
        cola.append(fuente)         # se encola el nodo fuente
        
        while cola:
            vertice = cola.pop(0)
            print(vertice, end=' ') # se procesa el vértice(aquí, imprimirlo)
            
            # se recorre todos los nodos adyacentes no visitados
            for adyacente in self.lista_adyacencia[vertice]:
                if not visitado[adyacente]:
                    visitado[adyacente] = True  # marca como visitado
                    cola.append(adyacente)      # se encola para futuras visitas

# ejemplo: crea un objeto grafo con 6 vertices de 0 a 5
g = Grafo(6)

# agrega aristas desde el vértice 2
g.agregar_arista(0,1)
g.agregar_arista(0,2)
g.agregar_arista(1,2)
g.agregar_arista(2,0)
g.agregar_arista(2,3)
g.agregar_arista(3,3)
g.agregar_arista(3,4)
g.agregar_arista(4,5)

# realiza el BFS desde el vértice 2
print("Recorrido BFS iniciando desde el vértice 2: ")
g.BFS(1)