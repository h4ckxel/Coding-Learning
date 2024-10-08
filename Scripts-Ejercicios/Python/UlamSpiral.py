import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from PIL import Image, ImageTk

def sieve_of_eratosthenes(limit):
    """Devuelve una lista booleana donde True indica que el número es primo."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 y 1 no son primos
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for i in range(start*start, limit + 1, start):
                sieve[i] = False
    return sieve

def generate_ulam_spiral(n):
    x, y = 0, 0
    step = 1
    dx, dy = 0, -1
    positions = {}

    for i in range(1, n+1):
        positions[i] = (x, y)
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy

    return positions

def is_on_diagonal(x, y):
    """Determina si un punto (x, y) cae en una línea diagonal."""
    return x == y or x == -y

def draw_spiral(batch_size):
    global current_step, is_paused
    if is_paused:
        return
    prime_positions = []
    for i in range(batch_size):
        if current_step > max_steps:
            return

        num = current_step
        x, y = spiral_positions[num]

        if sieve[num]:
            prime_positions.append((x, y))
            # números primos en diagonal con azul, los demás en rojo
            if is_on_diagonal(x, y):
                ax.plot(x, y, 'bo')  # puntos en la diagonal en azul
            else:
                ax.plot(x, y, 'ro') 
        else:
            ax.plot(x, y, 'go', markersize=2)  # los demás números en verde pequeño
        
        current_step += 1

    if len(prime_positions) > 1:
        prime_positions = np.array(prime_positions)
        ax.plot(prime_positions[:, 0], prime_positions[:, 1], 'g-', linewidth=1)

    ax.set_aspect('equal')
    canvas.draw()

def update_spiral():
    global batch_size
    draw_spiral(batch_size)
    
    if current_step <= max_steps:
        root.after(30, update_spiral)  # controlador de velocidad

def start_spiral():
    global is_paused
    is_paused = False
    update_spiral()

def pause_spiral():
    global is_paused
    is_paused = True

def reset_spiral():
    global current_step, is_paused
    is_paused = True
    current_step = 1
    ax.cla()  
    canvas.draw()

def zoom(event):
    """Función para hacer zoom en la gráfica."""
    scale_factor = 1.2
    if event.delta > 0:
        ax.set_xlim([x / scale_factor for x in ax.get_xlim()])
        ax.set_ylim([y / scale_factor for y in ax.get_ylim()])
    elif event.delta < 0:
        ax.set_xlim([x * scale_factor for x in ax.get_xlim()])
        ax.set_ylim([y * scale_factor for y in ax.get_ylim()])
    canvas.draw()

def start_pan(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def pan(event):
    """Función para navegar por la gráfica (pan)."""
    dx = (event.x - start_x) / 100  # velocidad del desplazamiento
    dy = (event.y - start_y) / 100

    ax.set_xlim(ax.get_xlim() - dx)
    ax.set_ylim(ax.get_ylim() - dy)
    canvas.draw()

def add_text():
    """Añade un texto explicativo sobre la espiral de Ulam."""
    info_text = ("La espiral de Ulam: \n"
                "Colocando los números naturales en una espiral y \n"
                "marcando los números primos, se revelan patrones diagonales. \n\n"
                "Dato curioso: la espiral de Ulam fue descubierta por \n"
                "Stanislaw Ulam en 1963 mientras se aburría en una reunión. \n"
                "Este fenómeno sigue siendo un misterio matemático.\n\n"
                "Creado por h4ckxel")
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, info_text)
    text_widget.config(state=tk.DISABLED)

'''def add_ulam_image():
    """Coloca la imagen de Ulam debajo del texto."""
    image = Image.open('/mnt/data/image.png')
    image = image.resize((200, 200), Image.ANTIALIAS)
    ulam_photo = ImageTk.PhotoImage(image)

    label = ttk.Label(text_frame, image=ulam_photo)
    label.image = ulam_photo  # Guardar referencia para que no sea recolectado por el garbage collector
    label.pack(side=tk.BOTTOM, pady=10)'''

# ventana principal
root = tk.Tk()
root.title("Espiral de Ulam con Primos Conectados")

# marco principal
frame = ttk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# matplotlib
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

canvas.get_tk_widget().bind("<MouseWheel>", zoom)
canvas.get_tk_widget().bind("<ButtonPress-1>", start_pan)
canvas.get_tk_widget().bind("<B1-Motion>", pan)

text_frame = ttk.Frame(root)
text_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

text_widget = tk.Text(text_frame, width=40, height=20, wrap=tk.WORD, padx=10, pady=10)
text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
text_widget.config(state=tk.DISABLED) 

# botones de control
control_frame = ttk.Frame(root)
control_frame.pack(side=tk.TOP, pady=10)

start_button = ttk.Button(control_frame, text="Iniciar Espiral", command=start_spiral)
start_button.pack(side=tk.LEFT, padx=5)

pause_button = ttk.Button(control_frame, text="Pausar Espiral", command=pause_spiral)
pause_button.pack(side=tk.LEFT, padx=5)

reset_button = ttk.Button(control_frame, text="Reiniciar Espiral", command=reset_spiral)
reset_button.pack(side=tk.LEFT, padx=5)

add_text()
#add_ulam_image()

max_steps = 10000  # máximo de números a mostrar en la espiral
current_step = 1
batch_size = 50  
is_paused = False

spiral_positions = generate_ulam_spiral(max_steps)

sieve = sieve_of_eratosthenes(max_steps)

root.mainloop()
