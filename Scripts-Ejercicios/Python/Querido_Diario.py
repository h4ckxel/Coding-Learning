import tkinter as tk
from tkinter import scrolledtext, messagebox
import datetime
import os
import json

# Configuración del archivo de almacenamiento
DATA_FILE = "diario.json"

def cargar_entradas():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_entrada():
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texto = entrada_texto.get("1.0", tk.END).strip()
    if texto:
        entradas[fecha] = texto
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(entradas, f, ensure_ascii=False, indent=4)
        messagebox.showinfo("Guardado", "Entrada guardada correctamente")
        entrada_texto.delete("1.0", tk.END)

def ver_entradas():
    ventana_historial = tk.Toplevel(root)
    ventana_historial.title("Historial de Entradas")
    ventana_historial.geometry("600x400")
    
    historial_texto = scrolledtext.ScrolledText(ventana_historial, wrap=tk.WORD, width=100, height=50)
    historial_texto.pack(padx=10, pady=10)
    
    for fecha, texto in sorted(entradas.items(), reverse=True):
        historial_texto.insert(tk.END, f"[{fecha}]:\n{texto}\n{'-'*50}\n")
    historial_texto.config(state=tk.DISABLED)

# Cargar entradas previas
entradas = cargar_entradas()

# Configurar la ventana principal
root = tk.Tk()
root.title("Diario Personal")
root.geometry("1500x1400")
root.configure(bg="#222")

titulo = tk.Label(root, text="Diario Personal", font=("Arial", 24), fg="white", bg="#222")
titulo.pack(pady=10)

entrada_texto = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=300, height=65)
entrada_texto.pack(padx=10, pady=10)

btn_guardar = tk.Button(root, text="Guardar Pensamiento", command=guardar_entrada, bg="#444", fg="white")
btn_guardar.pack(pady=5)

btn_ver = tk.Button(root, text="Ver Pensamientos", command=ver_entradas, bg="#444", fg="white")
btn_ver.pack(pady=5)

root.mainloop()
