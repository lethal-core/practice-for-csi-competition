import numpy

l1 = []
l2 = []

for _ in range(2):
    for i in range(3):
        l = []
        for j in range(3):
            print(f"Enter the element ({i+1},{j+1}): ", end="")
            x = int(input())
            l.append(x)
        if _ == 0:
            l1.append(l)
        else:
            l2.append(l)
        
matrix1 = numpy.array(l1)
matrix2 = numpy.array(l2)

print()
print("Matrix 1: ")
print(matrix1)
print()
print("Matrix 2: ")
print(matrix2)
print()

sum = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    sum.append(row)
    
sum_matrix = numpy.array(sum)

print("Matrix 1 + Matrix 2: ")
print(sum_matrix)
print()

product = []

for k in range(3):
    row = []
    for i in range(3):
        element = 0
        for j in range(3):
            element += matrix1[k][j] * matrix2[j][i]
        row.append(element)
    product.append(row)

product_matrix = numpy.array(product)

print("Matrix 1 x Matrix 2: ")
print(product_matrix)