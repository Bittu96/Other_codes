sample_matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sample_matrix_2 = [
    [1,  2,  3, 4],
    [5,  6,  7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

sample_matrix_3 = [
    [1,  2,  3,  4,   5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# one rotation = 90 degree rotation anti clock-wise


def matrix_rotation(matrix, rotations):
    side = len(matrix)

    # number of loops to be rotated
    no_of_loops = side//2

    for loop in range(no_of_loops):

        # loop specific co-ordinates
        row_first, row_last = loop, side-1-loop
        col_first, col_last = loop, side-1-loop

        # 1 rotation is equal to (row_last-row_first) shifts in a loop
        # n rotations is equal to n*(row_last-row_first) shifts in a loop
        total_shifts = rotations*(row_last-row_first)

        for _ in range(total_shifts):
            hold = "this_is_the_hold_value"

            # top side shift
            for i in range(col_first, col_last+1):
                matrix[i][row_first], hold = hold, matrix[i][row_first]

            # right side shift
            for i in range(row_first+1, row_last+1):
                matrix[col_last][i], hold = hold, matrix[col_last][i]

            # bottom side shift
            for i in range(col_last-1, col_first-1, -1):
                matrix[i][row_last], hold = hold, matrix[i][row_last]

            # left side shift
            for i in range(row_last-1, row_first-1, -1):
                matrix[col_first][i], hold = hold, matrix[col_first][i]

    return matrix


rotated_matrix = matrix_rotation(sample_matrix_1, 1)
print(*rotated_matrix, sep="\n")

print()

rotated_matrix = matrix_rotation(sample_matrix_2, 1)
print(*rotated_matrix, sep="\n")

print()

rotated_matrix = matrix_rotation(sample_matrix_3, 1)
print(*rotated_matrix, sep="\n")

'''
solution: 

[3, 6, 9]
[2, 5, 8]
[1, 4, 7]

[4, 8, 12, 16]
[3, 7, 11, 15]
[2, 6, 10, 14]
[1, 5, 9, 13]

[5, 10, 15, 20, 25]
[4, 9, 14, 19, 24]
[3, 8, 13, 18, 23]
[2, 7, 12, 17, 22]
[1, 6, 11, 16, 21]

'''