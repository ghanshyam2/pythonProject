def subArraySum(arr, k):
    dicts = {0: 1}
    total, count = 0, 0

    for i in range(len(arr)):
        total += arr[i]

        if total - k in dicts:
            count += dicts[total - k]
        if total in dicts:
            dicts[total] += 1
        else:
            dicts[total] = 1
    return count


print(subArraySum([10, 2, -2, -20, 10], -10))
print(subArraySum([9, 4, 20, 3, 10, 5], 33))
# Complexity = O(N)
# Space Complexity = O(1)
