#!/bin/bash

# Función para implementar la Criba de Eratóstenes
criba_eratostenes() {
    local limite=$1
    local i j

    # Inicializar el array de números primos
    local -a primos
    for ((i=2; i<=limite; i++)); do
        primos[i]=1
    done

    # Aplicar la criba
    for ((i=2; i*i<=limite; i++)); do
        if [ ${primos[i]} -eq 1 ]; then
            for ((j=i*i; j<=limite; j+=i)); do
                primos[j]=0
            done
        fi
    done

    # Imprimir los números primos
    echo "Números primos hasta $limite:"
    for ((i=2; i<=limite; i++)); do
        if [ ${primos[i]} -eq 1 ]; then
            echo -n "$i "
        fi
    done
    echo
}

# Verificar que se ha proporcionado un argumento
if [ $# -eq 0 ]; then
    echo "Uso: $0 <limite>"
    exit 1
fi

# Llamar a la función con el límite proporcionado
criba_eratostenes $1
