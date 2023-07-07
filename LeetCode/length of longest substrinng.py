def length_longest_subString(arr, k):
    start, maxLen, maxOnes = 0, 0, 0

    for end in range(len(arr)):
        if arr[end] == 1:
            maxOnes += 1

        if (end - start + 1 - maxOnes) > k:
            if arr[start] == 1:
                maxOnes -= 1
            start += 1
        maxLen = max(maxLen, end - start + 1)
    return maxLen


print(length_longest_subString([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(length_longest_subString([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
