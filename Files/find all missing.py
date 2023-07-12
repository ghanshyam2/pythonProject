def find_all_missing(arr):
    start = 0
    end = len(arr)
    while start < end:
        first = arr[start] - 1

        if arr[start] != arr[first]:
            arr[start], arr[first] = arr[first], arr[start]
        else:
            start += 1
    missing = []
    for i in range(end):
        if arr[i] != i + 1:
            missing.append(i + 1)
    return missing


print(find_all_missing([1, 2, 0]))
print(find_all_missing([2, 4, 1, 2]))
print(find_all_missing([2, 3, 2, 1]))

# TC = O(N)
# SC = O(1)
