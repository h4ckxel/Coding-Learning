# visualizacion de los grafos
class Graph:
    def __init__(self, num_nodes, directed=False, labels=None): # direct=False (false grafo no dirigido, true dirigido)
        self.adj_list = [[] for _ in range(num_nodes)]          # lista de adyacencia vacia
        self.directed = directed                                # si el grafo es dirigido o no
        self.labels = labels if labels else [str(i) for i in range(num_nodes)]
        
    # metodo para añadir una arista entre dos nodos
    def add_edge(self, node1, node2):
        if node2 not in self.adj_list[node1]:
            self.adj_list[node1].append(node2)
        if not self.directed and node1 not in self.adj_list[node2]:
            self.adj_list[node2].append(node1)
    
    # metodo par visualizar letras
    def print_graph(self):
        for i, neighbors in enumerate(self.adj_list):
        # for i in range(len(self.adj_list)):
        #   print("en le indice [i]")
        #   print("en le indice lista[i]")
            neighbor_labels = '->'.join(self.labels[neighbor] for neighbor in neighbors)
            print(f"Nodo {self.labels[i]}: {neighbor_labels}")
            
# grafo no dirigido con etiquetas de letras
labels_undirected = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
noditos = len(labels_undirected)
dirigido = False
graph_undirected = Graph(num_nodes=noditos, directed=dirigido, labels=labels_undirected)

# se añaden aristas
for i in range(noditos):
    print(f"El primer nodo es: {labels_undirected[i]}.")
    a = int(input("¿Cuántos vecinos tiene? "))
    
    for _ in range(a):
        vecino = input(f"Ingrese el nodo vecino de {labels_undirected[i]}: ").upper()
        if vecino in labels_undirected:
            j = labels_undirected.index(vecino)
            graph_undirected.add_edge(i, j)
        else:
            print("Nodo no válido, inténtelo de nuevo.")

# Imprimir el grafo
graph_undirected.print_graph()

# graph_undirected.add_edge(0,1) # A->B
# graph_undirected.add_edge(0,2) # A->C
# graph_undirected.add_edge(0,3) # A->D
# graph_undirected.add_edge(0,1) # B->E
# graph_undirected.add_edge(0,1) # C->G
# graph_undirected.add_edge(0,1) # D->H
# graph_undirected.add_edge(0,1) # E->I
# graph_undirected.add_edge(0,1) # F->I
# graph_undirected.add_edge(0,1) # G->J
# graph_undirected.add_edge(0,1) # H->K
# graph_undirected.add_edge(0,1) # J->K