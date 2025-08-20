a = input("Enter elements separated by spaces: ")
a = a.split()
a = [int(i) for i in a]
b = input("Enter elements separated by spaces: ")
b = b.split()
b = [int(i) for i in b]

res = []

for i in b:
    if i in a:
        for j in range(a.count(i)):
            res.append(i)
        while i in a:
            del a[a.index(i)]

res.extend(sorted(a))

for i in res:
    print(i,end=' ')