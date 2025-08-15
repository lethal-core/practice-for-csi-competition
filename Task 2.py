import numpy

l1 = []

m = int(input("Enter the number of columns in the matrix: "))
n = int(input("Enter the number of rows in the matrix: "))
print()

for i in range(m):
    l = []
    for j in range(n):
        print(f"Enter the element ({i+1},{j+1}): ", end="")
        x = int(input())
        l.append(x)
    l1.append(l)
        
matrix = numpy.array(l1)

print()
print("Matrix: ", matrix)
print()
min = numpy.min(matrix)
print("Minimum element in the matrix is: ", min)
max = numpy.max(matrix)
print("Maximum element in the matrix is: ", max)
print()

transpose = []

for i in range(n):
    l = []
    for j in range(m):
        l.append(matrix[j][i])
    transpose.append(l)

transpose_matrix = numpy.array(transpose)

print(transpose_matrix)