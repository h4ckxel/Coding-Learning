# funcion de la criba
def criba_eratostenes(limite):
    # array de números primos
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False  # 0 y 1 no son primos

    # criba
    for i in range(2, int(limite**0.5) + 1):
        if primos[i]:
            for j in range(i * i, limite + 1, i):
                primos[j] = False

    # impresion de numeros primos
    print(f"Números primos hasta {limite}:")
    for i in range(2, limite + 1):
        if primos[i]:
            print(i, end=" ")
    print()


# se pide al usuario que ingrese un limite
try:
    limite = int(input("Ingresa un número límite: "))
    if limite < 2:
        print("El número debe ser mayor o igual a 2.")
    else:
        criba_eratostenes(limite)
except ValueError:
    print("Por favor, ingresa un número entero válido.")
