def tripletSum(arr):
    n = len(arr)
    arr.sort()
    for i in range(n):
        left = i + 1
        right = n - 1

        while left < right:
            sums = arr[i] + arr[left] + arr[right]

            if sums == 0:
                return 1
            elif sums < 0:
                left += 1
            else:
                right -= 1
    return 0


print(tripletSum([0, -1, 2, -3, 1]))

# Complexity = O(N^2)
# Space Complexity = O(N)
