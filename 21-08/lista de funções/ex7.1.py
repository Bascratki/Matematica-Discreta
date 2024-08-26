import matplotlib.pyplot as plt
import numpy as np

def funcao2Grau(a, b, c, x):
    return a * x**2 + b * x + c

a, b, c = 1, -3, 2

x_values = np.linspace(-10, 10, 100)

y_values_2grau = funcao2Grau(a, b, c, x_values)

fig = plt.figure(figsize=(8, 6))

plt.scatter(x_values, y_values_2grau, color='blue', label='Discreta')
plt.plot(x_values, y_values_2grau, color='red', label='Contínua')

plt.title('Função do 2º Grau: f(x) = ax² + bx + c')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

plt.show()



