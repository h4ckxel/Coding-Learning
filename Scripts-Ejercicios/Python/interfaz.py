import tkinter as tk

root = tk.Tk()
root.title

expresion = ""

def presionar_boton(valor):
    global expresion
    expresion += str(valor)
    entrada_de_texto.set(expresion)
    
def calcular():
    global expresion
    try:
        resultado = evaluar_expresion(expresion)
        entrada_texto.set(str(resultado))
        expresion = str(resultado)
    
    except:
        entrada_texto.set("Error")
        expresion = ""
        
def borrar():
    global expresion
    expresion = ""
    entrada_texto.set("")
    
def evaluar_expresion(expresion):
    caracteres = list(expresion)
    numeros = []
    operadores = []
    
    numero_actual = ""
    for caracter in caracteres:
        if caracter.isdigit() or caracter == '.':
            numero_actual += caracter
        else:
            numeros.append(float(numero_actual))
            operadores.append(caracter)
            numero_actual = ""
    
    if numero_actual:
        numeros.append(float(numero_actual))
    
    i = 0
    while i < len(operadores):
        if operadores[i] == '*' or operadores[i] == '/':
            if operadores [i] == '*':
                resultado = numeros[i] * numeros[i+1]
        elif operadores[i] == '/':
            #### CUIDADO ####
            if numeros[i+1] == 0:
                raise ValueError("Division por cero")
            resultado = numeros[i] / numeros[i+1]
        numeros = numeros[:i] + [resultado] + numeros[i+2:]
        operadores = operadores[:i] + operadores[i+1:]
    else:
        i += 1
            
    i = 0
    while i < len(operadores):
        if operadores[i] == '+':
            resultado = numeros[i] + numeros[i+1]
        elif operadores[i] == '-':
            resultado = numeros[i] = numeros[i+1]
            
            numeros = numeros[:i] + [resultado] + numeros[i+2:]
            operadores = operadores[:i] + operadores[i+1:]