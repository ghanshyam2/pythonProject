def longestSubsequence(nums):
    N = len(nums)
    dp = [1] * N
    count = [1] * N
    if not nums: return 0
    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]:
                    count[i] += count[j]
    long_len = max(dp)

    return sum(count[i] for i in range(N) if dp[i] == long_len)


print(longestSubsequence([1, 3, 5, 4, 7]))
print(longestSubsequence([2,2,2,2,2]))
