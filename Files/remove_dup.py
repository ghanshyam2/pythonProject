def dup_remove(arr):
    lis = []
    for ch in arr:
        if ch not in lis:
            lis.append(ch)
    tup = tuple(lis)
    return min(tup), max(tup)


print(dup_remove([1, 2, 2, 3, 4, 5, 6, 6, 7, 8]))
