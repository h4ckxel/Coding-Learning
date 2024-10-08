# Estructuras Dinámicas lineales
###### `8 de Octubre del 2024`
- Listas
- Pilas
- Colas
- Colas de prioridades
- Aplicación de algoritmos

### TDA: Tipo de Dato Abtracto

Un conjunto de ***operaciones*** que se puede realizar sobre un conjunto de datos.

#### **Conceptos clave**:

- Abstracto: Es un tipo de dato que se define por su comportamiento y no por su implementación.

En general un TDA se basa en las operaciones que soporta

1. Operaciones Constructoras. (POO) ---> Crean o inicializan un TDA
2. Operaciones de Acceso. ---> Permiten acceder o verificar datos en un TDA pero sin modificarlos.
3. Operaciones Mificadoras. ---> cambiar el estado del TDA de alguna manera. Borrar, Copiar, Eliminar.

---

## Pila (stack)
Una pila e un TDA que sigue la politica "*el último en entrar es el primero en salir*" LIFO (*Last In, First Out*)

#### Operaciones: 
- apilar ***push()***: Inserta un elemento
- eliminar ***pop()***: Elimina y retorna el elemento de la parte superior 
- husmear ***peek()***: Ver elemento de la parte de superior pero sin eliminarlo
- ¿Esta vacía? ***is_empty()***: Verifica si la pila esta vacía

PILA ----> lista aligada

Existe un ***Nodo Superior***

***Nodo***: Representa a un elemento de la pila. Este nodo tiene un dato de cualquier tipo y un apuntador a otro nodo que sera el que esta debajo de el.

`instancia = inicializar el constructor`

Cuando se crea una ***instancia*** de la pila no se deben enviar argumentos, ya que la misma pila ya inicializa con el nodo superior vacio. 

---

## Ejemplo

```python

```












---
