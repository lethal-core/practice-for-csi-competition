N = int(input("Enter Target Amount: "))
m = int(input("Enter the number of denominations: "))
coins = input("Enter the list of coin denominations separated by spaces: ")
coins = coins.split()
coins = [int(i) for i in coins]

l = [0] * (N + 1)
l[0] = 1

for coin in coins:
    for amount in range(coin, N + 1):
        l[amount] += l[amount - coin]

print(l[N])