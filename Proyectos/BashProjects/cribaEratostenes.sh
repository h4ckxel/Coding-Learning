#!/bin/bash

# funcion de la Criba
criba_eratostenes() {
    local limite=$1
    local i j

    # array de numeros primos
    local -a primos
    for ((i=2; i<=limite; i++)); do
        primos[i]=1
    done

    # se aplica criba
    for ((i=2; i*i<=limite; i++)); do
        if [ ${primos[i]} -eq 1 ]; then
            for ((j=i*i; j<=limite; j+=i)); do
                primos[j]=0
            done
        fi
    done

    # impresion de numeros primos
    echo "Números primos hasta $limite:"
    for ((i=2; i<=limite; i++)); do
        if [ ${primos[i]} -eq 1 ]; then
            echo -n "$i "
        fi
    done
    echo
}

# verificacion del argumento dado por el usuario
if [ $# -eq 0 ]; then
    echo "Uso: $0 <limite>"
    exit 1
fi

# llamar la funcion con el limite que digito el usuario
criba_eratostenes $1
