import matplotlib.pyplot as plt
import numpy as np

def funcaoModular(x):
    return np.abs(x)

x_values = np.linspace(-10, 10, 100)

y_values_modular = funcaoModular(x_values)

fig = plt.figure(figsize=(8, 6))

plt.scatter(x_values, y_values_modular, color='blue', label='Discreta')
plt.plot(x_values, y_values_modular, color='red', label='Contínua')

plt.title('Função Modular: f(x) = |x|')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

plt.show()



