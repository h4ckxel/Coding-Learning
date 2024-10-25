class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adyacencia = [[] for _ in range(num_vertices)]
        
    # método
    def agregar_arista(self, origen, destino):
        self.lista_adyacencia[origen].append(destino) # se agrega el destino a la lista de origen
        # para grafo no dirigido
        #self.lista_adyacencia[destino].append(origen) # se agrega el origen a la lista de destino
        
        # metodo auxiliar para DFS recursivo
    def dfs_aux(self, vertice, visitado): 
        visitado[vertice] = True            # marca el vértice como visitado
        print(vertice, end=" ")             # se procesa el vértice
        
        for adyacente in self.lista_adyacencia[vertice]:
            if not visitado[adyacente]:
                self.dfs_aux(adyacente, visitado) # llamada recursiva
                
    # método para realizar DFS
    def DFS(self, fuente):
        visitado = False * self.num_vertices
        self.dfs_aux(fuente, visitado)


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
print("Recorrido DFS iniciando desde el vértice 2: ")
g.DFS(2)
            
        
        