def search_element_array(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(search_element_array([10, 6, 4, 3], 3))
print(search_element_array([10, 6, 4, 3], 6))
print(search_element_array([10, 6, 4, 3], 10))
