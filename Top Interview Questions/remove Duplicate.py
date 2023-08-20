def removeDuplicate(nums):
    non_duplicate_idx = 1
    i = 1
    while i < len(nums):
        if nums[non_duplicate_idx - 1] != nums[i]:
            nums[non_duplicate_idx] = nums[i]
            non_duplicate_idx += 1
        i += 1
    return non_duplicate_idx


print(removeDuplicate([1, 1, 2]))
print(removeDuplicate([0,0,1,2,3,4,5,6,5,6,7]))
