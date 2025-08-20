s = input("Enter String: ")

longest = 0

for i in range(len(s)):
    for j in range(1,len(s)):
        a = s[i:j]
        if a == a[::-1] and len(a) > longest:
            longest = len(a)

print(longest)