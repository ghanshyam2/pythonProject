def twoSum(nums, target):
    dict1 = {}

    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in dict1:
            return [i, dict1[comp]]
        dict1[nums[i]] = i


print(twoSum([2, 7, 11, 15], 9))
