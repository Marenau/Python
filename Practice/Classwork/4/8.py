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
    return det(submatrix(A, i, j))


def alg(A, i, j):
    return minor(A, i, j) * (-1) ** (i + j)


def algmatrix(A):
    res = [[0] * len(A) for _ in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[i][j] = alg(A, i, j)
    return res


def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def inv(A):
    trans_a = transpose(algmatrix(A))
    det_a = det(A)
    res = [[0] * len(trans_a) for _ in range(len(trans_a[0]))]
    for i in range(len(trans_a)):
        for j in range(len(trans_a[0])):
            res[i][j] = trans_a[i][j] / det_a
    return res

def mult(A, B):
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def moore_penrose(H):
    return mult(inv(mult(transpose(H), H)), transpose(H))


A = [[0, 2, 1, 4],
     [1, 0, 3, 2],
     [0, 1, 4, 0],
     [1, 2, 1, 1]]


print(moore_penrose(A))
