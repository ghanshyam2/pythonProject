def mergeString(word1, word2):
    n = len(word1)
    m = len(word2)
    res = []
    i = 0
    j = 0
    while i < n and j < m:
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1
    res.append(word1[i:])
    res.append(word2[j:])
    return "".join(res)


print(mergeString('abc', 'pqr'))
print(mergeString('ab', 'pqr'))
