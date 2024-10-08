// TAREA HACERLO CON EL BUCLE WHILE
#include <stdio.h>

int main() {
    int num, i, factorial = 1;
    printf("Ingresa un número para calcular el factorial: ");
    scanf("%d", &num);
    
    if (num < 0) {
        printf("No hay factoriales negativos.\n");
    } else {
        for(i = 1; i <= num; ++i){
            factorial *= i;
        }
        printf("El factorial de %d! es: %d\n", num, factorial);
    }
    return 0;
}
