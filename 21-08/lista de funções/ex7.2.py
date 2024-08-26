import matplotlib.pyplot as plt
import numpy as np

def funcaoExponencial(a, b, x):
    return a * b**x

a_exp, b_exp = 2, 1.5

x_values = np.linspace(-10, 10, 100)

y_values_exponencial = funcaoExponencial(a_exp, b_exp, x_values)

fig = plt.figure(figsize=(8, 6))

plt.scatter(x_values, y_values_exponencial, color='blue', label='Discreta')
plt.plot(x_values, y_values_exponencial, color='red', label='Contínua')

plt.title('Função Exponencial: f(x) = a.b^x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

plt.show()



