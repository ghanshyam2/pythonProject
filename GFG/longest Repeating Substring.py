def longestRepeatingSubstring(string):
    dp = [[-1 for i in range(len(string) + 1)] for j in range(len(string) + 1)]

    return lrs(string, 0, 0, dp)


def lrs(s1, i, j, dp):
    if i >= len(s1) or j >= len(s1):
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if dp[i][j] == -1:

        if s1[i] == s1[j] and i != j:

            dp[i][j] = 1 + lrs(s1, i + 1, j + 1, dp)

        else:

            dp[i][j] = max(lrs(s1, i, j + 1, dp),

                           lrs(s1, i + 1, j, dp))

    return dp[i][j]


print(longestRepeatingSubstring("axxyxz"))
