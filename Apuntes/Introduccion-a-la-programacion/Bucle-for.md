# Bucle for
`2 / Octubre / 2024`

### Sintaxis:

```C
    - for(inicialización ; condición lógica ; Inc/dec){
    Instrucciones;
    }
```

### Ejemplo
```C
int main(){
    int i;
    for(i = 1 ; i <= 10; i++){
        printf("%d". i);
    }
    return 0;
}

>>>> 1 2 3 4 5 6 7 8 9
```
### Sumatoria de los primeros 100 numeros
```C
#include <stdio.h>

int main(){
    int i, sum=0;
    for(i=1;i<=100;i++){
        sum += i;
    }
    printf("La sumatoria es: %d", sum);
    return 0;
}
```