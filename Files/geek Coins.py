def geekCoins(n):
    coin = 0

    for i in range(1, n+1):
        if i % 8 == 0:
            coin += 9
        else:
            coin += 1
    return coin


print(geekCoins(15))
print(geekCoins(365))
print(geekCoins(30))
