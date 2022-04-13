# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_matrix(matrix):
    matrix_len = len(matrix)
    # Transpose of the matrix
    for i in range(matrix_len):
        for j in range(i, matrix_len):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Swap the matrix
    for i in range(matrix_len):
        for j in range(matrix_len // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][matrix_len - 1 -  j]
            matrix[i][matrix_len - 1 -  j] = temp

    return matrix

input_matrix = [[1, 2],
                [4, 3]]
print(rotate_matrix(input_matrix))