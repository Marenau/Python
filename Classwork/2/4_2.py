def transpose_matrix(matrix):
    transposed_matrix = []
    for i in range(len(matrix)):
        transposed_matrix.append([])
        for j in range(len(matrix[0])):
            transposed_matrix[i].append(matrix[j][i])
    return transposed_matrix

matrix = [[0, 1, 0], [2, 0, 1], [1, 3, 1]]

transposed_matrix = transpose_matrix(matrix)

print(row for row in transposed_matrix)
