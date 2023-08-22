def removeDuplicates(nums):
    i = 0
    n = len(nums)
    streak = 1
    for j in range(n):
        c = nums[j]
        if j > 0 and c == nums[j - 1]:
            streak += 1
        else:
            streak = 1
        if streak <= 2:
            nums[i] = nums[j]
            i += 1

    return i


print(removeDuplicates([1, 1, 1, 2, 2, 3]))
