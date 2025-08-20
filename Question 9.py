l = input("Enter elements separated by spaces: ")
l = l.split()
l = [int(i) for i in l]

combinations = []

for i in l:
    for j in l:
        if i != j and [i,j] not in combinations:
            combinations.append([i,j])

minimun = combinations[0][0] - combinations[0][1]
if minimun < 0:
    minimun = 0 - minimun
combi = combinations[0]

for combination in combinations:
    a = combination[0] - combination[1]
    if a < 0:
        a = 0 - a
    if minimun > a and a != 0:
        minimun = a
        combi = combination

for i in combi:
    print(i,end=' ')