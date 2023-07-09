def powerOfNumber(n):
    newNum = n
    mod = 10 ** 9 + 7
    rev = 0
    while n != 0:
        dig = n % 10
        rev = rev * 10 + dig
        n //= 10
    return (newNum ** rev) % mod


print(powerOfNumber(2))
print(powerOfNumber(12))
print(powerOfNumber(15))
