k = int(input("Enter the value of k: "))
l = input("Enter elements separated by spaces: ")
l = l.split()
l = [int(i) for i in l]

combinations = []

for i in range(len(l)):
    for j in range(i + 1, len(l) + 1):
        combinations.append(l[i:j])

count = 0

for combination in combinations:
    if sum(combination) == k:
        count += 1

print(count)