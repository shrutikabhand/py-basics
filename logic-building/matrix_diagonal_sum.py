# This program calculates the sum of the principal diagonal elements of a matrix.
# The user first enters the size of the square matrix.
# Matrix elements are then stored row by row in a nested list.
# A loop is used to access and add the diagonal elements where row index equals column index.
# Finally, the program prints the sum of the diagonal elements.



N = int(input())

matrix = []

for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

sum_diagonal = 0

for i in range(N):
    sum_diagonal += matrix[i][i]
print(sum_diagonal)

