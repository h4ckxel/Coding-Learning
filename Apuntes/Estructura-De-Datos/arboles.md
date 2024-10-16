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
3. Árbol equilibrado (***tambien es un árbol binario***): Todas las hojas estan como maximo un nivel de diferencia
4. Árbol completo: es árbol equilibrado y ademas las hojasdel ultimo nivel estan a lo mas a la izquierda posible.
5. Árbol lleno: Árbol completo y ademas tiene las hojas del ultimo nivel.

---

### Operaciones
En general:

  * Create() ----> Árbol ----> Devuelve un árbol vacio. (intanciar un arbol de la clase arbol)
  * Add(Element) ----> Árbol ----> Devuelve un árbol al agregar un elemento
  * Remove() ----> Árbol ----> Devuelve un árbol despues de borrar un elemento

### Árboles Binarios Balanceados (**ABB**)

Árboles AVL:

Balanceado; para cada nodo se tiene que cumplir que:
   - **B < A < C** 
   - Como programar un árbol binario balanceado.

Se llama AVL si cumple las siguientes caracteristicas:

* Para cada nodo, la diferencia de alturas entre sus subárboles izquierdo y derecho (***factor de balanceo***) no puede ser mayor a 1.
* Las operaciones de inserción y eliminación requieren _rotaciones_ para mantener el balance.

### Operaciones AVL

  * Create() ----> Árbol ----> Devuelve un árbol vacio. (intanciar un arbol de la clase arbol)
  * Add(Element) ----> Árbol ----> Devuelve un árbol al agregar un elemento
  * Remove() ----> Árbol ----> Devuelve un árbol despues de borrar un elemento

#### Operacionesde recorrido
* Preorder()
* Inorder()
* Postorder()

El problema radica al momento de agregar/remover elementos -> es probable que se desbalanceé.

Para ello se necesitan de dos operaciones más.

* rotateLeft() ----> Árbol ----> Devuelve un árbol rotado a la izquierda
* rotateRight() ----> Árbol ----> Devuelve un árbol rotado a la derecha

### Rotaciones
Sucede cunado al agregarle o quitarle un elemento a un AVL, se desbalancea.














