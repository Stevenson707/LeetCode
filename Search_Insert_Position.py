def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    if len(nums) == 1:
        if nums[0] < target:
            return target - nums[0]
        if nums[0] > target:
            return 0
    for i in range(len(nums) - 1):
        if nums[i] < target and nums[i + 1] > target:
            return nums.index(nums[i + 1])
        if nums[-1] < target:
            return nums.index(nums[-1]) + 1
        if nums[0] > target:
            return 0


print(searchInsert([1, 3, 5, 6], 7))
