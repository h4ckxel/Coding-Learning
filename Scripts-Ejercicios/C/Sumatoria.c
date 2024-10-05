#include <stdio.h>

int main(){
    int i, s=0;
    for(i=1;i<=100;i++){
    	s += i;
	}
	printf("La sumatoria de los primeros 100 numeros es: %d", s);
    return 0;
}
