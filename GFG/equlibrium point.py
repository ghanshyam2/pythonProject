def equilibriumPoint(A):
    start = 0
    total = sum(A)

    for ind, val in enumerate(A):
        end = total - start - val
        if end == start:
            return ind + 1
        start += val

    return -1


print(equilibriumPoint([1, 3, 5, 2, 2]))
print(equilibriumPoint([1]))
