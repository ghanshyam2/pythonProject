def transpose(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if col >= row:
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    return matrix


print(transpose([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]))
# complexity = O(N*N)
# SC = O(1)
