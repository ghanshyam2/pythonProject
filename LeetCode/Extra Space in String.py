def minExtraChar(s, dictionary):
    m = len(s)
    dicts_set = set(dictionary)
    dp = [0] * (m + 1)
    for start in range(m - 1, -1, -1):
        dp[start] = 1 + dp[start + 1]
        for end in range(start, m):
            curr = s[start: end + 1]
            if curr in dicts_set:
                dp[start] = min(dp[start], dp[end + 1])
    return dp[0]


print(minExtraChar("leetscode", ["leet", 'code', "leetcode"]))
