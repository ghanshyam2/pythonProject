def candyDist(ratings):
    res = [1] * len(ratings)
    for i in range(len(ratings) - 1):
        if ratings[i] < ratings[i + 1]:
            res[i + 1] = res[i] + 1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            res[i] = max(res[i + 1] + 1, res[i])
    return sum(res)


print(candyDist([1, 0, 2]))
print(candyDist([1, 2, 2]))
