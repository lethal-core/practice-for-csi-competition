k = int(input("Enter k: "))
l = input("Enter elements separated by spaces: ")
l = l.split()
l = [int(i) for i in l]

for i in range(k-1):
    a = max(l)
    while a in l:
        l.remove(a)
    
print(max(l))