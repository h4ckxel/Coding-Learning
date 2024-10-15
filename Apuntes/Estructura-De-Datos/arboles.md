# Árbol
###### `15 de Octubre del 2024`
- Es una estructura dinámica no lineal.
- Es una estructura jerarquica
### Definicion
Estructura de datos jerarquica compuesto por nodos conectados entre si.

Un arbol se define por:
- Nodo Raiz (***Root***)
  - Es el nodo superior del cual parten todas las ramas.
- Nodos
  - Cada nodo del arbol contiene un **valor** o un **dato** y puede tener en general nodos hijos (***subarboles***). 
  - Un nodo puede ser: 
    - Nodo padre: Si tiene uno o mas nodos hijos conectados a el.
    - Nodo hijo: Si esta conectado a otro nodo superior.
- Hojas (leaps)
  - Son nodos que no tiene nodos hijos. Se encuentran al final de las ramas del árbol.
- Altura de un árbol
  - Es el número máximo de niveles dado la raiz hasta una hoja
- Nivel de un nodo
  - Distancia que hay desde la raíz hasta el nodo. La raíz esta en el nivel cero.
- Grado de un nodo
  - Es el número de hijos que tiene un nodo.
- Subárbol
  - Es un árbol cualquier estructura que parte de un nodo y contiene a sus descendientes
- RECURSIVIDAD
  - Los árboles se pueden definir de manera recursiva:
    - un arbol es un nodo raíz que tiene uno o mas subarboles, donde cada subarbol es un arbol

---

<div align="center">

<img src="https://ingenieriabasica.es/wp-content/uploads/2019/08/Euler-abstracci%C3%B3n.png" width="80%"/>

</div>

---

### Clasificación de los arboles: Depende de su estrucutura y sus restricciones

1. Árbol generico: No hay restricciones en su estructura.
2. Árbol binario: Cada nodo tiene a lo mas dos nodos.
   1. izquierdo <---- hijos ----> derecho
3. 