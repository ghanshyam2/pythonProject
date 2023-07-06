def occurrence_find(lis):
    sets = {}
    for ch in lis:

        if ch not in sets:
            sets[ch] = 1
        else:
            sets[ch] += 1
    return sets


print(occurrence_find([11, 45, 8, 11, 23, 45, 23, 45, 89]))
