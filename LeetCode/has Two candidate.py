def hasTwoCandidate(arr, k):
    a = 1
    for i in range(len(arr) - 1):
        if arr[i] + arr[a] == k:
            return True
        a += 1
    else:
        return False


print(hasTwoCandidate([1, 2, 3, 4, 5, 6], 11))
