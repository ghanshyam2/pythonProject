def uniqueFrequency(arr):

    dicts = {}
    for ar in arr:
        if ar in dicts:
            dicts[ar] += 1
        else:
            dicts[ar] = 1
    lists = list(dicts.values())
    if len(set(lists)) == len(lists):
        return True
    else:
        return False


print(uniqueFrequency([2, 2, 5, 10, 1, 2, 10, 5, 10, 2]))
print(uniqueFrequency([1, 1, 2, 5, 5]))
