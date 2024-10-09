# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:59:42 2024

@author: Lenovo
"""

class Estudiante:
    def __init__(self, nombre = str, edad = float, promedio = float):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
        
# se crea un registro de un estudiante
estudiante1 = Estudiante("Pancho", 21, 9.6)

# se acceden a los campos del registro
print(f"Nombre: {estudiante1.nombre}")
print(f"Edad: {estudiante1.edad}")
print(f"Promedio: {estudiante1.promedio}")

print("--------------------------------")
# modificacion del valor de un campo
estudiante1.promedio = 6        
print(f"Nombre: {estudiante1.nombre}")
print(f"Edad: {estudiante1.edad}")
print(f"Promedio: {estudiante1.promedio}")
    
