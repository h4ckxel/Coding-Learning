// Comentarios
// Esto es un comentario de una línea
/* Esto es un 
   comentario de múltiples líneas */

// Declaración de variables
var nombre = "Acxel"; // Variable global (obsoleta, evitar su uso)
let edad = 20; // Variable de bloque (recomendado)
const PI = 3.1416; // Constante (no se puede reasignar)

// Tipos de datos primitivos
let numero = 42; // Número
let texto = "Hola, mundo"; // String
let booleano = true; // Booleano
let nulo = null; // Nulo
let indefinido; // Undefined

// Tipos de datos complejos
let arreglo = [1, 2, 3, 4, 5]; // Array
let objeto = { nombre: "h4ckxel", edad: 20 }; // Objeto

// Operadores básicos
let suma = 10 + 5;
console.log(suma);

let resta = 10 - 5;
console.log(resta);

let multiplicacion = 10 * 5;
console.log(multiplicacion);

let division = 10 / 5;
console.log(division);

let modulo = 10 % 3;
console.log(modulo);

let exponente = 2 ** 3;
console.log(exponente);

// Operadores de comparación
let igual = (10 == "10"); // true (compara valor)
let estrictamenteIgual = (10 === "10"); // false (compara valor y tipo)
let diferente = (10 != 5);
let mayorQue = (10 > 5);
let menorQue = (10 < 5);

// Estructuras de control
if (edad >= 18) {
    console.log("Eres mayor de edad");
} else {
    console.log("Eres menor de edad");
}

// Switch
let dia = "lunes";
switch (dia) {
    case "lunes":
        console.log("Inicio de semana");
        break;
    case "viernes":
        console.log("Fin de semana");
        break;
    default:
        console.log("Día normal");
}

// Bucles
for (let i = 0; i < 5; i++) {
    console.log("Iteración", i);
}

let contador = 0;
while (contador < 5) {
    console.log("While loop", contador);
    contador++;
}

do {
    console.log("Do-while loop", contador);
    contador++;
} while (contador < 10);

// Funciones
function saludar(nombre) {
    return "Hola, " + nombre;
}
console.log(saludar("Acxel"));

// Funciones flecha
const sumar = (a, b) => a + b;
console.log(sumar(3, 4));

// Objetos y métodos
let persona = {
    nombre: "H4ckxel",
    edad: 20,
    saludar: function () {
        return "Hola, soy " + this.nombre;
    }
};
console.log(persona.saludar());

// Manejo del DOM (si se ejecuta en un navegador)
// document.getElementById("miElemento").textContent = "Nuevo texto";

// Console para depuración
console.log("Mensaje en consola");
console.error("Esto es un error");
console.warn("Esto es una advertencia");
