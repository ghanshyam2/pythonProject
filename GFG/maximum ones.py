def maxOnes(a):
    ans, one, zero = 0, 0, 0

    for num in a:
        if num == 1:
            zero -= 1
            one += 1
        else:
            zero += 1
        ans = max(zero, ans)
        zero = max(0, zero)
    return one + ans


print(maxOnes([1, 0, 0, 1, 0]))
print(maxOnes([0,1,1,0,1,1,1]))
