def squareRoot(x):
    start, end = 0, x
    ans = - 1

    while start <= end:
        mid = start + (end - start) // 2
        sq = mid * mid

        if sq == x:
            return mid
        if sq < x:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans


print(squareRoot(5))
print(squareRoot(10))
print(squareRoot(4))
