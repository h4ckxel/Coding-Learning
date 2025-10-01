#include <stdio.h>

int main(){
	int a,b,c,n,i;
	a=0;
	b=1;

	printf("Digita hasta que numero quieres calcular la serie de Fibonacci: ");
	scanf("%d", &n);
	printf("%d %d ", a, b);

	for (i=1;i<=n;i++){
    c=a+b;
    printf("%d ",c);
    a=b;
    b=c;
	}     
return 0;
}
