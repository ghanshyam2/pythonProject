def coinChange(coin, nt, amount):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if nt <= 0:
        return 0

    return coinChange(coin, nt - 1, amount) + coinChange(coin, nt , amount - coin[nt - 1])


coins = [1, 2, 3]
n = len(coins)
print(coinChange(coins, n, 4))
