from itertools import chain, combinations

C = {2, 3, 4}

def todos_subconjuntos(conjunto):
    s = list(conjunto)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

subconjuntos = list(todos_subconjuntos(C))

print("Subconjuntos de C:")
for subconjunto in subconjuntos:
    subconjunto_set = set(subconjunto)
    print(f"{subconjunto_set} é subconjunto de C: {subconjunto_set.issubset(C)}")


