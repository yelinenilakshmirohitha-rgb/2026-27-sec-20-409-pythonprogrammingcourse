A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Matrix Addition:")
for i in range(2):
    for j in range(2):
        print(A[i][j] + B[i][j], end=" ")
    print()

print("Matrix Subtraction:")
for i in range(2):
    for j in range(2):
        print(A[i][j] - B[i][j], end=" ")
    print()