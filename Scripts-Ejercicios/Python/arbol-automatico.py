# función para generar nodos de un árbol de decisión simulado
def build_tree(data, depth=0):
    # caso base: si no hay más profundidad o todos los resultados son iguales, retornar una hoja
    if depth == 0 or len(set(data)) == 1:
        return data[0]  # retorna la primera clase

    # simulamos la división de los datos en base a alguna condición
    mid_point = len(data) // 2  # punto medio como "umbral" para dividir
    left_data = data[:mid_point]
    right_data = data[mid_point:]

    # construir el árbol recursivamente
    left_branch = build_tree(left_data, depth - 1)
    right_branch = build_tree(right_data, depth - 1)

    # retornamos el nodo actual con sus dos ramas
    return (left_branch, right_branch)

# función para simular la clasificación
def classify(tree, index):
    # recorrer el árbol simulando decisiones
    node = tree
    while isinstance(node, tuple):
        if index < len(node[0]):
            node = node[0]  # ir por la rama izquierda
        else:
            node = node[1]  # ir por la rama derecha
    return node

# ejemplo de uso
data = ['class1', 'class1', 'class2', 'class2']  # datos simulados con dos clases
decision_tree = build_tree(data, depth=2)  # construimos el árbol
result = classify(decision_tree, 1)  # clasificamos un dato
print(result)  # salida: class1
