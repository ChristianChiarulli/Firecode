def flip_horizontal_axis(matrix):
    row = len(matrix) - 1
    col = len(matrix[0]) - 1

    temp = 0

    i = 0

    while i <= row/2:
        j = 0
        while j <= col:
            temp = matrix[i][j]
            matrix[i][j] = matrix[row-i][j]
            matrix[row-i][j] = temp
            j = j+1
        i = i + 1

flip_horizontal_axis()
