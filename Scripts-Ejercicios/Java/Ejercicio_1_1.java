public static void main(String args[]) {
int masa = 91; // Masa en kilogramos
double estatura = 1.77; // Estatura en metros
double IMC = masa/Math.pow(estatura, 2); /* Calcular el índice 
de masa corporal */
System.out.println(“La persona tiene una masa = “ + masa + “ 
kilogramos y estatura = “ + estatura + “ metros”); /* Mediante 
varios if-else anidados se evalúan diferentes rangos del IMC */
if (IMC < 16) {
System.out.println(“La persona tiene delgadez severa.”);
} else if (IMC < 17) {
System.out.println(“La persona tiene delgadez moderada.”);
} else if (IMC < 18.5) {
System.out.println(“La persona tiene delgadez leve.”);
} else if (IMC < 25) {
System.out.println(“La persona tiene peso normal.”);
} else if (IMC < 30) {
System.out.println(“La persona tiene sobrepeso.”);
} else if (IMC < 35) {
System.out.println(“La persona tiene obesidad leve.”);
} else if (IMC < 40) {
System.out.println(“La persona tiene obesidad media.”);
} else {
System.out.println(“La persona tiene obesidad mórbida.”);
}
}