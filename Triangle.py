def minimumTotal(triangle):
    num_rows = len(triangle)
    min_path_sum = [0] * (num_rows + 1)
    for row in range(num_rows - 1, -1, -1):
        for col in range(row + 1):
            min_path_sum[col] = min(min_path_sum[col], min_path_sum[col + 1]) + triangle[row][col]
    return min_path_sum[0]


print(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(minimumTotal([[-10]]))
print(minimumTotal([[-1], [2, 3], [1, -1, -3]]))



# def minimumTotal(triangle):
#     summ = [triangle[0][0]]
#     results = []
#     index = 0
#     for row in range(1, len(triangle)):
#         for item in range(len(triangle[row]) - 1):
#             if item == index:
#                 summ.append(min(triangle[row][item], triangle[row][item + 1]))
#                 index = item
#     return sum(summ)