def largestPrimeFactor(N):
    res = float('inf')
    num = 2

    while num * num <= N:
        while N % num == 0:
            res = num
            N //= 2
        num += 1
    if N > 1:
        return N
    return res


print(largestPrimeFactor(5))
print(largestPrimeFactor(36))
