from itertools import combinations

C = {2, 3, 4}

# Generate all the subsets of C
subsets = []
for i in range(len(C) + 1):
    subsets.extend(set(combinations(C, i)))

# Test and print the results
for subset in subsets:
    if subset.issubset(C):
        print(f"{subset} is a subset of C")
    else:
        print(f"{subset} is not a subset of C")