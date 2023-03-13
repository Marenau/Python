def submatrix(A, a, b):
    sub = []
    for i in range(len(A)):
        if i != a:
            temp = []
            for j in range(len(A[0])):
                if j != b:
                    temp.append(A[i][j])
            sub.append(temp)
    return sub


A = [[0, 2, 1],
     [1, 4, 3],
     [2, 1, 1]]

print(submatrix(A, 0, 0))
print(submatrix(A, 1, 1))
print(submatrix(A, 2, 1))
