'''
from bubble_sort import * el asterisco es para llamar todas las funciones de ese codigo o una especifica y llamar AS como un alias
Hacer un programa que ordene una lista de estudiantes
segun su promedio
. Usar registro como clase
. Llenar base de datos con al menos 10 estudiantes
. Ordenarlos de menor a mayor promedio (burbuja)
. Ordenar basado en un criterio
'''

class Estudiante:
    def __init__(self, nombre = str, edad = float, promedio = float):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

# Funcion par ordenar
def ordenarPromedio(estudiantes):
    n = len(estudiantes)

    for i in range(n):
        for j in range(0, n-i-1):
            if estudiantes[j].promedio > estudiantes[j+1].promedio:
                #arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                estudiantes[j], estudiantes[j+1] = estudiantes[j+1], estudiantes[j]

def ordenarEdad(estudiantes):
    n = len(estudiantes)

    for i in range(n):
        for j in range(0, n-i-1):
            if estudiantes[j].edad > estudiantes[j+1].edad:
                # arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                estudiantes[j], estudiantes[j+1] = estudiantes[j+1], estudiantes[j]

                
def printEstudiante(estudiante):
        for estudi in estudiante:
            print(f"Nombre: {estudi.nombre}\nPromedio: {estudi.promedio}\nEdad: {estudi.edad}\n--------------------")   
        
# Base de datos
baseDeDatos = [
            Estudiante("Rogelio", 21, 6.8),
            Estudiante("Laura", 18, 7.8),
            Estudiante("Luis", 22, 9.9),
            Estudiante("Jose", 32, 5.4),
            Estudiante("Betriz", 25, 7.7),
            Estudiante("Richie", 22, 6.9),
            Estudiante("Carmen", 21, 9.1),
            Estudiante("Pedro", 21, 8.4),
            Estudiante("El chato", 21, 7.2),
            Estudiante("Ana", 19, 9.0),
            ]
print("\nLa lista de estudiantes es:\n")
printEstudiante(baseDeDatos)
ordenarPromedio(baseDeDatos)
# Imprimir la lista ordenada por promedio
print("\tLista de estudiantes ordenada por promedio (de menor a mayor):\n")
for estudiante in baseDeDatos:
    print(f"Nombre: {estudiante.nombre}\nPromedio: {estudiante.promedio}\nEdad: {estudiante.edad}\n----------------------------------------")

# Imprimir la lista ordenada por edad
ordenarEdad(baseDeDatos)
print("\n\tLista de estudiantes ordenada por edad (de menor a mayor):\n")
for estudiante in baseDeDatos:
    print(f"Nombre: {estudiante.nombre}\nPromedio: {estudiante.promedio}\nEdad: {estudiante.edad}\n----------------------------------------")
