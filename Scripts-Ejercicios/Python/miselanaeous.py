import matplotlib.pyplot as plt # es de uso general, se usa para graficar, y es principalmente usada en ciencia de datos
import numpy as np

p = int(input("Dame el valor de p: "))
h = float(input("Dame el valor de h: "))
k = float(input("Dame el valor de k: "))

'''
Dominio = [-10, 10], de 0.1,
- 10
- 9.9
- 9.8
- 9.7
- 9.6
entre mas puntos, mas suave es la curva
'''

#x1 = [i/10 for i in range(-100, 101)] #compresion de listas
x3 = np.linspace(-10, 10, 201)#compresion de listas
# print(x1)
print(x3)

#y1 = [4*p*(x1[i] - h)**2 + k for i in range(-100, 101)]
y2 = 4*p*(x3 - h)**2 + k
y3 = 4*p*(x3 - h)**2 + k

plt.plot(x3, y2, color='red', linewidth=4)
plt.scatter(h, k, color='black', linewidth=2)
plt.scatter(h, k+p, color='black', linewidth=2)
plt.show()

# numerical python
# x2 = np.arange(-10, 10, 0.1) compre2sion de listas
# print(x2)

# numerical python