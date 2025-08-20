s = input("Enter string: ")

d = {}

for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

f = True

c = d[s[0]]

for i in d:
    if d[i] != c:
        f = False

if f:
    print("YES")
else:
    print("NO")