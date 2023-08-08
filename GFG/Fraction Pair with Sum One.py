from math import gcd


def fractionPairWithSum1(numerator, denominator):
    count = 0
    dicts = {}
    for val, ind in zip(numerator, denominator):
        gVal = gcd(val, ind)

        val //= gVal
        ind //= gVal

        count += dicts.get((ind - val, ind), 0)
        dicts[(val, ind)] = dicts.get((val, ind), 0) + 1

    return count


print(fractionPairWithSum1([1, 2, 2, 8], [2, 4, 6, 12]))
print(fractionPairWithSum1([3, 1, 12, 81, 2], [9, 10, 18, 90, 5]))
