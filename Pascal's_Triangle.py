def generate(numRows):
    if numRows == 1:
        return [[1]]
    triangle = [[1], [1, 1]]
    for i in range(1, numRows - 1):
        next_row = [1]
        for j in range(len(triangle[i]) - 1):
            next_row.append(triangle[i][j] + triangle[i][j + 1])
        next_row.append(1)
        triangle.append(next_row)
    return triangle


print(generate(2))