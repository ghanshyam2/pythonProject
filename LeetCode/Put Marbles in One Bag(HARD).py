def putMarbles(weights, k):
    m = len(weights)
    weight = [0] * (m - 1)
    for i in range(m - 1):
        weight[i] = weights[i] + weights[i + 1]
    weight.sort()

    result = 0
    for j in range(k - 1):
        result += weight[m - 2 - j] - weight[j]
    return result


print(putMarbles([1, 3, 5, 1], 2))
print(putMarbles([1, 3], 2))

# Complexity = O(N.LogN)
# Space Complexity = O(N)
