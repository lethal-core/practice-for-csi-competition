n = int(input("Enter no. of words: "))

words = []
for i in range(n):
    a = input("Enter word: ")
    words.append(sorted(a))

pairs = []
for word in words:
    if word not in pairs:
        pairs.append(word)

print(len(pairs))