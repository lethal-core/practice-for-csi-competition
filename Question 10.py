l = input("Enter elements separated by spaces: ")
l = l.split()
l = [int(i) for i in l]

for i in range(len(l)):
    prod = 1
    for j in range(len(l)):
        if i != j:
            prod *= l[j]
    print(prod,end=" ")