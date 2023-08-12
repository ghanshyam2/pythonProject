def search_ceiling(arr, key):
    arr.sort()
    n = len(arr)
    if key > arr[n - 1]:
        return -1

    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            return mid
    return left


print(search_ceiling([4, 6, 10], 6))
print(search_ceiling([1, 3, 8, 10, 15], 12))
print(search_ceiling([4, 6, 10], 13))
