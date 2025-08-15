n = int(input("Enter no. of elements: "))

arr = []

while len(arr) != n:
    print("Enter element", len(arr)+1, ": ", end="")
    x = int(input())
    if x == 0 or x == 1:
        arr.append(x)
    else:
        print("Invalid input. Please enter 0 or 1.")

print(arr)
print()

k = int(input("Enter the value of k: "))

left = 0
zero_count = 0
max_len = 0

for right in range(n):
    if arr[right] == 0:
        zero_count += 1
    while zero_count > k:
        if arr[left] == 0:
            zero_count -= 1
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)