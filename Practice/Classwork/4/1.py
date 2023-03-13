def smalldet(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


A = [[4, 3],
     [1, 1]]

print(smalldet(A))
