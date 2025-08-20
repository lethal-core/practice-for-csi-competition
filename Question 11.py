k = int(input("Enter the value of k: "))
l = input("Enter elements separated by spaces: ")
l = l.split()
l = [int(i) for i in l]

combinations = []

for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if i != j and i != k and j != k:
                combinations.append([l[i],l[j],l[k]])

count = 0

for combination in combinations:
    a = 0
    for i in combination:
        a += i
    if a % k == 0:
        count += 1

print(count)