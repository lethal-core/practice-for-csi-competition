n = int(input("Enter the number of integers: "))
l = input("Enter elements separated by spaces: ")
l = l.split()
l = [int(i) for i in l]

combinations = []

for i in range(len(l)):
    for j in range(i + 1, len(l) + 1):
        combinations.append(l[i:j])

longest = 0

for combination in combinations:
    f = 1
    if combination[0] <= 0:
        for i in range(0,len(combination),2):
            if combination[i] > 0:
                f = 0
        for i in range(1,len(combination),2):
            if combination[i] < 0:
                f = 0
    if combination[0] >= 0:
        for i in range(0,len(combination),2):
            if combination[i] < 0:
                f = 0
        for i in range(1,len(combination),2):
            if combination[i] > 0:
                f = 0
    if f == 1 and longest < len(combination):
        longest = len(combination)

print(longest)