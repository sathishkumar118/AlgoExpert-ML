"""
Write a function that takes in two matrices and returns the result after multiplying them together
"""
def sparse_matrix_multiplication(matrix_a, matrix_b):
    row_count = len(matrix_a)
    col_count = len(matrix_b[0])
    if len(matrix_a[0]) == len(matrix_b):
        com_count = len(matrix_b)
    else:
        return [[]]
    result = zeros = [ [0]*col_count for _ in range(row_count) ]
    for i in range(row_count):
        for j in range(col_count):
            curr = 0
            for k in range(com_count):
                curr += matrix_a[i][k]*matrix_b[k][j]
            result[i][j] = curr
    return result
