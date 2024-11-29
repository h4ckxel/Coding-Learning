#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:08:56 2024

@author: Acxel
"""

import tkinter as tk
from tkinter import ttk

"""
función para convertir entre las unidades de área basándose en los factores de conversión.
"""
def convertir_area(valor, from_unit, to_unit):
    # factores de conversión entre unidades
    factores_conversion = {
        "m²": {"m²": 1, "ha": 0.0001, "km²": 1e-6, "ft²": 10.7639, "yd²": 1.19599, "ac": 0.000247105},
        "ha": {"m²": 10000, "ha": 1, "km²": 0.01, "ft²": 107639, "yd²": 11959.9, "ac": 2.47105},
        "km²": {"m²": 1e6, "ha": 100, "km²": 1, "ft²": 1.07639e7, "yd²": 1.19599e6, "ac": 247.105},
        "ft²": {"m²": 0.092903, "ha": 9.2903e-6, "km²": 9.2903e-8, "ft²": 1, "yd²": 0.111111, "ac": 2.2957e-5},
        "yd²": {"m²": 0.836127, "ha": 8.36127e-5, "km²": 8.36127e-7, "ft²": 9, "yd²": 1, "ac": 0.000206612},
        "ac": {"m²": 4046.86, "ha": 0.404686, "km²": 0.00404686, "ft²": 43560, "yd²": 4840, "ac": 1},
    }

    # calcular la conversión utilizando los factores de conversión
    return valor * factores_conversion[from_unit][to_unit]

"""
función para actualizar las unidades disponibles cuando se selecciona 'Área'.
"""
def actualizar_unidades(*args):
    # unidades específicas para área
    unidades_area = ["m²", "ha", "km²", "ft²", "yd²", "ac"]
    
    # limpiar las opciones anteriores
    from_unit_combobox['values'] = unidades_area
    to_unit_combobox['values'] = unidades_area
    
    # establecer valores por defecto
    from_unit_combobox.set(unidades_area[0])
    to_unit_combobox.set(unidades_area[1])

"""
función para manejar el evento de conversión al hacer clic en el botón.
"""
def realizar_conversion():
    try:
        # obtener valores de entrada
        valor = float(entry_valor.get())
        from_unit = from_unit_combobox.get()
        to_unit = to_unit_combobox.get()

        # realizar la conversión
        resultado = convertir_area(valor, from_unit, to_unit)

        # mostrar el resultado en la etiqueta
        label_resultado.config(text=f"Resultado: {resultado:.4f} {to_unit}")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa un número válido.")

# crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Unidades de Área")
ventana.geometry("400x300")

"""
crear y organizar widgets de la interfaz
"""
# etiqueta para el valor
label_valor = tk.Label(ventana, text="Valor:")
label_valor.pack()

# entrada para el valor
entry_valor = tk.Entry(ventana)
entry_valor.pack()

# etiqueta para la unidad de origen
label_from_unit = tk.Label(ventana, text="Unidad de Origen:")
label_from_unit.pack()

# menú desplegable para la unidad de origen
from_unit_combobox = ttk.Combobox(ventana, state="readonly")
from_unit_combobox.pack()

# etiqueta para la unidad de destino
label_to_unit = tk.Label(ventana, text="Unidad de Destino:")
label_to_unit.pack()

# menú desplegable para la unidad de destino
to_unit_combobox = ttk.Combobox(ventana, state="readonly")
to_unit_combobox.pack()

# botón para realizar la conversión
boton_convertir = tk.Button(ventana, text="Convertir", command=realizar_conversion)
boton_convertir.pack()

# etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

"""
inicializar las unidades para la categoría de área
"""
actualizar_unidades()

# ejecutar el bucle principal de la aplicación
ventana.mainloop()
