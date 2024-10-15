def conjunto_potencia(conjunto):
  listaconjunto = list(conjunto)
  subconjuntos = []

  for i in range(2**len(listaconjunto)):
    subconjunto = []
    for k in range(len(listaconjunto)):
      print(f"i: {bin(i)} ^ {bin(1<<k)} = {bin(i & 1<<k)}")
      if i & 1<<k:
        subconjunto.append(listaconjunto[k])
    subconjuntos.append(subconjunto)
  return subconjuntos


subconjuntos = conjunto_potencia(set([1,2,3]))
print(subconjuntos)
