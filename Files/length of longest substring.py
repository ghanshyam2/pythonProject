def lengthOfLongestSubString(s):
    seen, n = set(), len(s)
    right, res = -1, 0
    for left in range(n):
        print(left, right, s[left: right + 1], seen)
        while right + 1 < n and s[right + 1] not in seen:
            right += 1
            seen.add(s[right])
        res = max(res, right - left + 1)
        print(s[left: right + 1])
        if right == n - 1:
            break
        seen.discard(s[left])
    return res


print(lengthOfLongestSubString('abcabcbb'))
