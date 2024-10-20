def twoSum(nums, target):
    a = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                a.append(i)
                a.append(j)
                return a
