n = int(input("Enter no. of elements: "))

arr = []

for i in range(n):
    print("Enter element", i+1, ": ", end="")
    arr.append(int(input()))

freq = {}

for ele in arr:
    if ele not in freq:
        freq[ele] = 1
    else:
        freq[ele] += 1

maxi = max(freq , key=freq.get)

if freq[maxi] > (n/2):
    print("Majority element is: ", maxi)