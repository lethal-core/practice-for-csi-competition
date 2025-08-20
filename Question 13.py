N = int(input("Enter a number: "))

digits = [int(i) for i in str(N)]

if N % sum(digits) == 0:
    print("YES")
else:
    print("NO")