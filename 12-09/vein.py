# lista de funcoes -
# letra a
# a = x é natural, par e menor que 10 = 2, 4, 6, 8
# b = x é primo e menor que 10 = 2, 3, 5, 7
# pip install matplotlib-venn
# importar os módulos
from matplotlib_venn import venn2
from matplotlib import pyplot as plt
#letra a
a = [2, 4, 6, 8]
b = [2, 3, 5, 7]
a = set(a)
b = set(b)
union = a.union(b)
print("só em a temos 4, 6 e 8, 3 elementos")
print("só em b temos 3, 5 e 7, 3 elementos")
print("em ambos temos 1 elemento")
print("letra a ")
print("a uniao de a com b é", union)
#venn2(subsets = (3, 3, 1), set_labels = ('Diagrama A', 'Diagrama B'))
# letra B
#pede o complementar da uniao de a e b, porem nao tem complementar, vou dizer que
são os reias diferentes de 2, 3, 4, 5, 6, 7, 8, que eé a uniao de a e b
print("-----")
print("letra B")
print("x|x != 2, 3, 4, 5, 6, 7, 8 v x c R")
print("ou pode ser um conjunto vazio {}")
# lera c
# intersecçao de a com b
print("----")
print("letra C")
intersection = a.intersection(b)
print("a intersecçao de a com b é ", intersection)
#venn2(subsets = (3, 3, 0), set_labels = ('Diagrama A', 'Diagrama B'))
print("---")
# letra d
print("letra D")
print("o complemento da uniao de a com b é")
uniao = a.union(b)
interseccao = a.intersection(b)
complementodeacomb = uniao - interseccao
print(complementodeacomb)
#venn2(subsets = (3, 3, 0), set_labels = ('Diagrama A', 'Diagrama B'))
# letra e
# muito abstrato por nao ter dado conjunto universal
# vou colocar os elementos do complemento de b como todos naturais menor que 10
exceção os primos
print("----")
b = [1, 4, 6, 8]
interseccao = a.intersection(b)
#venn2(subsets = (1, 1, 3), set_labels = ('Diagrama A', 'Diagrama B'))
print("---")
print("lera f")
a = [2, 4, 6, 8]
a = [1, 3, 5, 7, 9]
b = [2, 3, 5, 7]
a = set(a)
interseccao = a.intersection(b)
venn2(subsets = (2, 1, 3), set_labels = ('Diagrama A', 'Diagrama B'))
plt.show()
