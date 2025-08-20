l = input("Enter elements separated by spaces: ")
l = l.split()

ele = l[0]
count = l.count(l[0])

for i in l:
    if count < l.count(i):
        ele = i
        count = l.count(i)

if count > len(l)/2:
    print(ele)
else:
    print("-1")