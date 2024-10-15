original_set = [1,2,3]
subsets = [[]]
# getting all the subsets for set
for num in original_set:
    num_options = []
    for subset in subsets:
        temp = subset.copy()
        temp.append(num)
        num_options.append(temp)
    subsets = subsets + num_options
# stating all of them are indeed subsets (to demonstrate issubset())
original_set = set(original_set)
for subset in subsets:
    subset = set(subset)
    if not subset.issubset(original_set):
        continue

    
print(f"O conjunto {subset or {}} é subconjunto de {original_set}")
print("total subsets: {}".format(len(subsets)))