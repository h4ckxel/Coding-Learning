//============================================================================
// Name        : ImplicitCasting.cpp
// Author      : Acxel Martin Elizalde Camacho
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;


void divEntera(){
	// c = b/a;
	int a=10, b=2;
	float c=0;
	c = b/a;

	cout<<"\nDivision Entera";
	cout<<"\n\t resultado: "<<c<<endl;
}

void divFlotante(){
	// c = b/a;
	float a=10, b=2, c=0;
	c = b/a;

	cout<<"\nDivision Flotante";
	cout<<"\n\t resultado: "<<c<<endl;
}

void divMixta(){
	// c = b/a;
	int a=10;
		float b=2.0;
		float c = b/a;

	cout<<"\nDivision Mixta";
	cout<<"\n\t resultado: "<<c<<endl;
}

void explicitTypeCasting(){
	// c = b/a;
	int a=10, b=2;
	float c;
	c = b/(float)a;

	cout<<"\nDivision Explicit Type Casting";
	cout<<"\n\t resultado: "<<c<<endl;
}



int main() {

	divEntera();
	divFlotante();
	divMixta();
	explicitTypeCasting();
	return 0;
}
