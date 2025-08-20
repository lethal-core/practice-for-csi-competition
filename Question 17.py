k = int(input("Enter the value of k: "))
l = input("Enter elements separated by spaces: ")
l = l.split()
l = [int(i) for i in l]

freq = {}

for i in l:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

freq_l = list(freq.keys())
freq_l2 = list(freq.values())

res = []

while len(res) < k:
    m = max(freq_l2)
    a = freq_l2.count(m)
    r = []
    for i in range(a):
        x = freq_l2.index(m)
        r.append(freq_l[x])
        del freq_l[x],freq_l2[x]
    for i in sorted(r):
        res.append(i)

for i in res[:k]:
    print(i,end=" ")