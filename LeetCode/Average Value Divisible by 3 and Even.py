def averageValueEven(nums):
    arr = []
    for even in nums:
        if even % 2 == 0 and even % 3 == 0:
            arr.append(even)
    if not arr:
        return 0
    return sum(arr) // len(arr)


print(averageValueEven([1, 3, 6, 10, 12, 15]))
print(averageValueEven([1, 2, 4, 7, 10]))
print(averageValueEven([3, 6, 9, 12, 15, 18, 21, 24]))
