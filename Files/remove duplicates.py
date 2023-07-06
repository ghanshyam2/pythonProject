def fun(s):
    sets = []

    for i in s:
        if i not in sets:
            sets.append(i)
    #return "".join(sets)
    return sets


print(fun("aaabbbcdefghiiij"))