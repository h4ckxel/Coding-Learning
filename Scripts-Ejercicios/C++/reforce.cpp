#include <iostream>
#include <conio.h>
using namespace std;

int printMenu(){
	int opc = -1;
	do{
	cout<<"\tCalculadora de Fracciones"<<endl;
	cout<<"1) Suma"<<endl;
	cout<<"2) Resta"<<endl;
	cout<<"3) Multiplicacion"<<endl;
	cout<<"4) Division"<<endl;
	cout<<"0) Salir"<<endl;
	cout<<"Ingresar opcion: "<<endl; cin>>opc;
	} while(opc<0 || opc>4);	
	return opc;
}

int main(){
	int opc = -1;
	
	while(opc != 0){
		opc = printMenu();
	}
	
	
	return 0;
}


