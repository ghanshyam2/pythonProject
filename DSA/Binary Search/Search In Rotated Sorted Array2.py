def search_in_rotated_sorted_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:

        while left < right and nums[left] == nums[left + 1]:
            left += 1
        while left < right and nums[right] == nums[right - 1]:
            right -= 1
        mid = (left + right) // 2
        if nums[mid] == target:
            return True

        elif nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return False


print(search_in_rotated_sorted_array([2, 5, 6, 0, 0, 1, 2], 0))
print(search_in_rotated_sorted_array([2, 5, 6, 0, 0, 1, 2], 3))
print(search_in_rotated_sorted_array([2,5,6,0,0,1,2],2))
