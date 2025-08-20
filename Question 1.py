def check_palindrome(s):
    freq = {}
    
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    l = freq.values()

    odd_count = 0

    for i in l:
        if i % 2 != 0:
            odd_count += 1

    if (len(s) % 2  == 0 and odd_count == 0) or (len(s) % 2 == 1 and odd_count == 1):
        return True
    return False

S = input("Enter String: ")

f = 0

if check_palindrome(S):
    f = 1

for i in range(len(S)-1):
    a = S[:i] + S[i+1:]
    if check_palindrome(a):
        f = 1

if f == 1:
    print("YES")

else:
    print("NO")