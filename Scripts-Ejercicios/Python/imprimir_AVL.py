from AVL import ArbolAVL, NodoAVL

def imprimir_arbol(raiz, nivel=0, prefijo="Raiz"):
    if raiz is not None:
        balance = arbol.obtener_balance(raiz)
        print(" " * (nivel*4) + prefijo + f"{raiz.valor} (altura: {raiz.altura}, Balance: {balance})")
        imprimir_arbol(raiz.izquierdo, nivel+1, prefijo="Izq")
        imprimir_arbol(raiz.derecho, nivel+1, prefijo="Der")

if __name__ == "__main__":
    arbol = ArbolAVL()
    valores = [30,20,40,10,25,35,50,5,65]
    for valor in valores:
        arbol.raiz = arbol.insertar(arbol.raiz, valor)
    imprimir_arbol(arbol.raiz)