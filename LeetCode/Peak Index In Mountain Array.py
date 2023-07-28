def peakIndexInMountainArray(arr):
    n = len(arr)

    start, end = 0, n - 2
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid - 1] > arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


print(peakIndexInMountainArray([0, 1, 0]))
print(peakIndexInMountainArray([0, 10, 5, 2]))
