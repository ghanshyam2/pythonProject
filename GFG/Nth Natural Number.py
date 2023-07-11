def NthNatural(N):
    ans, multiplier = 0, 1

    while N > 0:
        ans += multiplier * (N % 9)

        N //= 9
        multiplier *= 10
    return ans


print(NthNatural(9))
