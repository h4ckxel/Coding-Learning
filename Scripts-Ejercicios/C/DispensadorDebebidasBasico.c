/* A partir del algoritmo, diseñar el diagrama de flujo, pseudocódigo
y programa en C que permita obtener un refresco de una máquina automática
expendedora de bebidas embotelladas.

Ejercicio: A partir del algoritmo, diseñar el diagrama de flujo, pseudocódigo y programa en C que permita 
obtener un refresco de una máquina automática expendedora de bebidas embotelladas.

1. Inicio
2. Verificar el panel de bebidas, ubicando la bebida deseada.
3. Identificar el costo de la bebida.
4. Seleccionar la bebida deseada.
5. Mostar la bebida deseada seleccionada por el usuario
6. Introducir en la ranura correspondiente la cantidad monetaria que así corresponda a la bebida deseada,
 de preferencia introducir la cantidad exacta.
7. Si existe producto y se introdujo la cantidad exacta, entonces. En la bandeja de salida saldrá la bebida seleccionada.
8. Sino, si cantidad introducida es menor al precio de producto entonces. En el panel visualizará efectivo insuficiente.
9. Si cantidad introducida es mayor al precio de producto entonces.
Devolverá el efectivo de diferencia en la bandeja pertinente.
10. Fin
*/
//NO USAR METODOS

#include<stdio.h>

int main(){
	
	int opc;
	float ingreso, cambio; 

	printf("\t********MENU DE OPCIONES********");
	printf("\n\t1. Coca-Cola .... $20");
	printf("\n\t2. Agua      .... $10");
	printf("\n\t3. Jugo      .... $16");
	printf("\n\t4. Sprite    .... $18");
	printf("\nSeleccione una opcion: ");
	scanf("%d", &opc);
	
	switch(opc){
		//Caso 1: Coca-Cola
		case 1:
		if (ingreso > 20){
		cambio = ingreso - 20;
		printf("\nSu cambio es %.2f$, Gracias por su compra!", cambio);
		}
		else if (ingreso == 20){

		printf("\nUsted ha seleccionado: Coca-Cola\nTotal a pagar: 20$\nIntroduzca cantidad de dinero a pagar: ");
		scanf("%f", &ingreso);
		
				printf("\nGracias por su compra!");
			}
			else{
				printf("\nNo tiene fondos suficientes.");
			}; break;
		//Caso 2: Agua
		case 2:
		printf("\nUsted ha seleccionado: Agua\nTotal a pagar: 10$\nIntroduzca cantidad de dinero a pagar: ");
		scanf("%f$", &ingreso);
		
			if (ingreso > 10){
				cambio = ingreso - 10;
				printf("\nSu cambio es %.2f$, Gracias por su compra!", cambio);
			}
			else if (ingreso == 10){
				printf("\nGracias por su compra!");
			}
			else{
				printf("\nNo tiene fondos suficientes.");
			}; break;
		//caso 3: Jugo
		case 3:
		printf("\nUsted ha seleccionado: Jugo\nTotal a pagar: 16$\nIntroduzca cantidad de dinero a pagar: ");
		scanf("%f$", &ingreso);
		
			if (ingreso > 16){
				cambio = ingreso - 16;
				printf("\nSu cambio es %.2f$, Gracias por su compra!", cambio);
			}
			else if (ingreso == 16){
				printf("\nGracias por su compra!");
			}
			else{
				printf("\nNo tiene fondos suficientes.");
			}; break;
		//caso 4: Sprite
		case 4:
		printf("\nUsted ha seleccionado: Sprite\nTotal a pagar: 18$\nIntroduzca cantidad de dinero a pagar: ");
		scanf("%f$", &ingreso);
		
			if (ingreso > 18){
				cambio = ingreso - 18;
				printf("\nSu cambio es %.2f$, Gracias por su compra!", cambio);
			}
			else if (ingreso == 18){
				printf("\nGracias por su compra!");
			}
			else{
				printf("\nNo tiene fondos suficientes.");
			}; break;
			//Caso DEFAULT
			default: printf("\nOpcion invalida."); break;
			
			
	}
	return 0;
}
