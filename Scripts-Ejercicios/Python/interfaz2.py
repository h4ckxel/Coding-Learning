import tkinter as tk

root = tk.Tk()
root.title("Calculadora")

expresion = ""
entrada_texto = tk.StringVar()

# Funciones
def presionar_boton(valor):
    global expresion
    expresion += str(valor)
    entrada_texto.set(expresion)
    
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
            if operadores[i] == '*':
                resultado = numeros[i] * numeros[i+1]
            elif operadores[i] == '/':
                if numeros[i+1] == 0:
                    raise ValueError("División por cero")
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
            resultado = numeros[i] - numeros[i+1]
        numeros = numeros[:i] + [resultado] + numeros[i+2:]
        operadores = operadores[:i] + operadores[i+1:]
        
    return numeros[0] if numeros else 0

# Interfaz gráfica
entrada = tk.Entry(root, textvariable=entrada_texto, font=('Arial', 18), justify='right', bd=10, insertwidth=4, width=14, borderwidth=4)
entrada.grid(row=0, column=0, columnspan=4)

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

fila = 1
columna = 0

for boton in botones:
    if boton == '=':
        boton = tk.Button(root, text=boton, padx=20, pady=20, font=('Arial', 18), command=calcular)
    else:
        boton = tk.Button(root, text=boton, padx=20, pady=20, font=('Arial', 18), command=lambda b=boton: presionar_boton(b))
    boton.grid(row=fila, column=columna, sticky="nsew")
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

boton_borrar = tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 18), command=borrar)
boton_borrar.grid(row=fila, column=0, columnspan=4, sticky="nsew")

root.mainloop()
