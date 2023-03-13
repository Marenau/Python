def smalldet(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


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


def det(A):
    n = len(A)
    if n == 2:
        return smalldet(A)
    else:
        result = 0
        for j in range(n):
            minor = submatrix(A, 0, j)
            sign = (-1) ** j
            result += sign * A[0][j] * det(minor)
        return result


def minor(A, i, j):
    return (-1) ** (i + j) * det(A)


A = [[0, 2, 1, 4],
     [1, 0, 3, 2],
     [0, 1, 4, 0],
     [1, 2, 1, 1]]

print(minor(A, 0, 1))
