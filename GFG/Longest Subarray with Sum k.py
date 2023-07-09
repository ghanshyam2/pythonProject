def longestSumK(arr, k):
    n = len(arr)
    mp = {}
    su = 0
    mx = 0
    for i in range(n):
        su += arr[i]
        if su == k:
            mx = max(mx, i + 1)
        rem = su - k
        if rem in mp:
            mx = max(mx, i - mp[rem])
        if su not in mp:
            mp[su] = i
    return mx


print(longestSumK([10, 5, 2, 7, 1, 9], 15))
