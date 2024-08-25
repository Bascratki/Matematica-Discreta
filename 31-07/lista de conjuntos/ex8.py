A = {1, 2, 3}
D = {5, 3, 4, 2, 1}
C = {1, 2, 3, 4, 5}

resultadoAC = A.issubset(C) and A != C

if resultadoAC == True:
    print("A é um subconjunto próprio de C")
else:
    print("A não é um subconjunto próprio de C")

resultadoDC = D.issubset(C) and D != C

if resultadoDC == True:
    print("D é um subconjunto próprio de C")
else:
    print("D não é um subconjunto próprio de C")



