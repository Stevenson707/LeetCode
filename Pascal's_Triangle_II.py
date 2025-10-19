def generate(rowIndex):
    if rowIndex == 0:
        return [1]
    triangle = [[1], [1, 1]]
    for i in range(1, rowIndex):
        next_row = [1]
        for j in range(len(triangle[i]) - 1):
            next_row.append(triangle[i][j] + triangle[i][j + 1])
        next_row.append(1)
        triangle.append(next_row)
    return triangle[rowIndex]


print(generate(20))