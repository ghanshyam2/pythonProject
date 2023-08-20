def countOddEven(arr):
    count, count1 = 0, 0

    for num in arr:
        if num % 2 == 0:
            count += 1
        else:
            count1 += 1
    return count1, count


print(countOddEven([1, 2, 3, 4, 5]))
