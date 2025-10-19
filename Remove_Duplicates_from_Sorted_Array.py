# def removeDuplicates(nums):
#     lenght = len(nums)
#     lst = nums[:]
#     c = 0
#     count = 0
#     for i in range(0, lenght - 1):
#         if nums[i] == nums[i + 1]:
#             count += 1
#         if i == lenght - 1:
#             c += count
#             for _ in range(count):
#                 lst.remove(nums[i])
#             count = 0
#         else:
#             c += count
#             for _ in range(count):
#                 lst.remove(nums[i])
#             count = 0
#     k = len(lst)
#     for _ in range(lenght - len(lst)):
#         lst.append('_')
#     return k, lst


def removeDuplicates(nums):
    i = 1

    for j in range(1, len(nums)):
        if nums[j] != nums[i - 1]:
            nums[i] = nums[j]
            i += 1

    return i


print(removeDuplicates([1, 1, 2]))
