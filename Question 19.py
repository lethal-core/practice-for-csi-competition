l = input("Enter elements separated by spaces: ")
l = l.split()
l = [int(i) for i in l]

combinations = [[]]
    
for element in l[1::]:
    new_subsets = [subset + [element] for subset in combinations]
    combinations.extend(new_subsets)

final_combinations = []

for i in range(len(combinations)):
    combinations[i].insert(0,l[0])
    if sum(combinations[i]) == len(l):
        f = 1
        for j in range(1,len(combinations[i])):
            if combinations[i][j] not in l[l.index(combinations[i][j-1]):l.index(combinations[i][j-1])+combinations[i][j-1]]:
                f = 0
        if f == 1:
            final_combinations.append(combinations[i])

if len(final_combinations) == 0:
    print("-1")

else:
    len_final = [len(i) for i in final_combinations]
    print(min(len_final))