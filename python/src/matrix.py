

class Matrix:
    """
    This class describes the matrix
    """
    def __init__(self, m, n, data):
        self.matrix = data
        self.m = m
        self.n = n

    def __str__(self):
        #s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        #return s + '\n'
        pass


def transpose_matrix(matrix):
    """
    This method transposes matrix in place
    :param matrix:
    :return:
    """
    row_num = len(matrix)
    col_num = len(matrix[0])

    new_matrix = [[0] * row_num for c in range(col_num)]
    print_matrix(matrix)
    for r in range(row_num):
        for c in range(col_num):
            new_matrix[c][r] = matrix[r][c]

    print_matrix(new_matrix)

def transpose_matrix_in_place(matrix):
    """
    This method transposes the matrix in place without
    the use of the external memory (except one element)
    :param matrix:
    :return:
    """
    row_num = len(matrix)
    col_num = len(matrix[0])


    # Check if the matrix is square
    if row_num == col_num:
        for c in range(col_num - 1):
            for r in range(c + 1, row_num):
                tmp = matrix[c][r]
                matrix[c][r] = matrix[r][c]
                matrix[r][c] = tmp
    else:
        # the matrix is not square
        pass


    return matrix

def cycle_based_transposition(matrix, M, N):
    """
    Performs cycle based matrix transposition
    :param matrix:
    :param N:
    :param M:
    :return:
    """
    Q = N * M - 1

    # perform data swapping
    for k in range(1, Q):
        # Generate cycles
        cycles = []
        c = k
        while True:
            c = c * N % Q
            cycles.append(c)
            if c == k:
                break

        # Move teh data in each cycle
        l = len(cycles)
        tmp = matrix[k]
        print(l, cycles)
        for i in reversed(range(1, l)):
            matrix[cycles[i]] = matrix[cycles[i-1]]
        matrix[cycles[0]] = tmp

    return matrix


def print_matrix(matrix, M, N):
    """
    This method prints the matrix
    :param matrix:
    :return:
    """
    for r in range(N):
        s = '['
        for c in range(M - 1):
            s += str(matrix[r][c]) + ', '
        s += str(matrix[r][N - 1]) + ']'
        print(s)
    return

if __name__ == "__main__":
    matrix = [[1, 2],
              [3, 4],
              [5, 6]]

    #m1 = transpose_matrix(matrix)
    #transpose_matrix_in_place(matrix)
    print_matrix(matrix, 3, 2)
    cycle_based_transposition(matrix, 3, 2)
    print_matrix(matrix, 3, 2)
