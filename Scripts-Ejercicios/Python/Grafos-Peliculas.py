class RecomendationGraph:
    def __init__(self, num_nodes):
        self.adj_list = [[] for _ in range(num_nodes)]
        self.labels = [""] * num_nodes # Etiquetas de nodos (usuarios y peliculas)

    # Metodos para establecer el nombre de cada nodo (usuarios y peliculas)
    def set_label(self, node, label):
        self.labels[node] = label

    # Metodo para agregar una arista entre un usuario y una pelicula
    def add_edge(self, user, movie):
        # Suponer que 'user' y 'movie' sin indices
        self.adj_list[user].append(movie)
        self.adj_list[movie].append(user)
        # Por ser grafo no dirigido

    # Metodo para imprimir el grafo
    def print_graph(self):
        for i in range(len(self.adj_list)):
            print("Nodo", self.labels[i], ":", end=" ")
            for neighbor in self.adj_list[i]:
                print(self.labels[neighbor], end=" -> ")
            print()

    # Metodo para recomendar peliculas a un usuario
    def recommend_movies(self, user):
        seen_movies = set(self.adj_list[user]) # Peliculas que el usuario ha visto
        recommendations = set()

        # Recorrer las peliculas vistas por el usuario
        for movie in self.adj_list[user]:
        # Revisar los otros usuarios que han visto esta pelicula
            for other_user in self.adj_list[movie]:
                if other_user != user:
                    # Agregar peliculas que no ha visto el usuario
                    for movie_recommendation in self.adj_list[other_user]:
                        if movie_recommendation not in seen_movies:
                            recommendations.add(movie_recommendation)
        # Convertir indices de peliculas a sus etiquetas
        return [self.labels[movie] for movie in recommendations]

# Crear el grafo de recomendaciones con 10 nodos (4 usuarios y 6 peliculas)
rec_graph = RecomendationGraph(num_nodes=10)

# Establecer etiquetas para usuarios y peliculas
labels = []
user = int(input("Cuantos nodos usuarios hay?\n"))
pelis = int(input("Cuantos nodos peliculas hay?\n"))

for i in range(user):
    labels.append("U"+str(i+1))
for i in range(pelis):
    labels.append('P' + str(i+1))

for i in range(len(labels)):
    rec_graph.set_label(i, labels[i])

# print(labels)
# labels = ['U1', 'U2', 'U3', 'U4', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6']

# Agregar relaciones de usuarios y peliculas
rec_graph.add_edge(0,4)     #U1 - P1
rec_graph.add_edge(0,5)     #U1 - P2
rec_graph.add_edge(1,5)     #U2 - P2
rec_graph.add_edge(1,6)     #U2 - P3
rec_graph.add_edge(2,6)     #U3 - P3
rec_graph.add_edge(2,7)     #U3 - P4
rec_graph.add_edge(3,4)     #U4 - P1
rec_graph.add_edge(3,8)     #U4 - P5
rec_graph.add_edge(3,9)     #U4 - P6

# Imprimir el grafo
print("Grafo de recomendaciones: ")
rec_graph.print_graph()

# Obtener recomendaciones para el usuario U1 (indice 0)

print("Recomendaciones para U1: ", rec_graph.recommend_movies(2))