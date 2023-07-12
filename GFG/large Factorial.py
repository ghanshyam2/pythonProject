def largeFactorial(lis):
    # n = len(lis)
    lists = []
    mod = 10 ** 9 + 7
    fact = [0] * (max(lis) + 1)
    fact[0] = 1
    fact[1] = 1
    for i in range(2, max(lis) + 1):
        fact[i] = fact[i - 1] * i % mod
    for i in lis:
        lists.append(fact[i])
    return lists


print(largeFactorial([0, 1, 2, 3, 4]))

# for num in lis:
#     fact = 1
#     while num !=0:
#         fact *= num
#         num -= 1
#     lists.append(fact)
# return lists
