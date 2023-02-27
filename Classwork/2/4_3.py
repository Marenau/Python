def multiply_matrices(matrix1, matrix2):
    result_matrix = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix


matrix1 = [[1, 2], [3, 4], [5, 6]]
matrix2 = [[1, 2, 3] , [4, 5, 6]]

result = multiply_matrices(matrix1, matrix2)
