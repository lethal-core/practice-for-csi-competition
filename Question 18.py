k = int(input("Enter the value of target: "))
l = input("Enter elements separated by spaces: ")
l = l.split()
l = [int(i) for i in l]

combinations = [[]]
    
for element in l:
    new_subsets = [subset + [element] for subset in combinations]
    combinations.extend(new_subsets)

f = 0
for combination in combinations:
    if sum(combination) == k:
        f = 1
        break

if f == 1:
    print("YES")
else:
    print("NO")