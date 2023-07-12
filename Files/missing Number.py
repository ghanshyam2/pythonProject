def find_missing_number(arr):
    first, last = 0, len(arr)

    while first < last:
        start = arr[first]
        if arr[first] < last and arr[first] != arr[start]:
            arr[first], arr[start] = arr[start], arr[first]
        else:
            first += 1
    # return arr

    for i in range(last):
        if arr[i] != i:
            return i

    return last


print(find_missing_number([2, 0, 1]))
print(find_missing_number([4, 0, 3, 1]))
print(find_missing_number([1, 2, 3, 4]))

# TS = O(N)
# SC = O(1)
