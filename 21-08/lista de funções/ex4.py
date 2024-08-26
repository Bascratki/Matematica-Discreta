import matplotlib.pyplot as plt
import numpy as np

def funcao1oGrau(a, b, x):
    return (a * x + b)

vetorX = np.arange(-5, 5, 1)
print("Vetor X:", vetorX)

a = 2
b = 5

vetorY = []

for x in vetorX:
    y = funcao1oGrau(a, b, x)
    vetorY.append(int(y))

print("Vetor Y:", vetorY)



