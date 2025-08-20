l = input("Enter elements separated by spaces: ")
l = l.split()
l = [int(i) for i in l]

combinations = []

for i in range(len(l)):
    for j in range(i+1,len(l)):
        combinations.append([l[i],l[j]])
    
def lcm(a,b):
    i = 1
    while True:
        if (a*i) % b == 0:
            return a*i
        i += 1

smallest = lcm(combinations[0][0],combinations[0][1])
pair = combinations[0]

for combination in combinations:
    if lcm(combination[0],combination[1]) < smallest:
        smallest = lcm(combination[0],combination[1])
        pair = combination

for i in pair:
    print(i,end=' ')