import matplotlib.pyplot as plt
import numpy as np

def funcaoSeno(x):
    return np.sin(x)

x_values = np.linspace(-10, 10, 100)

y_values_seno = funcaoSeno(x_values)

fig = plt.figure(figsize=(8, 6))

plt.scatter(x_values, y_values_seno, color='blue', label='Discreta')
plt.plot(x_values, y_values_seno, color='red', label='Contínua')

plt.title('Função Seno: f(x) = sen(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

plt.show()



