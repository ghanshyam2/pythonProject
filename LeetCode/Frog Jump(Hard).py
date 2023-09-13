def frogJump(stones):
    n = len(stones)
    dp = [[False] * (n + 1) for _ in range(n)]
    dp[0][1] = True

    for i in range(1, n):
        for j in range(i):
            sums = stones[i] - stones[j]
            if sums <= n and dp[j][sums]:
                dp[i][sums - 1] = True
                dp[i][sums] = True
                dp[i][sums + 1] = True
    return any(dp[-1])


print(frogJump([0, 1, 3, 5, 6, 8, 12, 17]))
print(frogJump([0, 1, 2, 3, 4, 8, 9, 11]))
