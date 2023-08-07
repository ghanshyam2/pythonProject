def generate_permutations(s):
    result = []
    generate_permutations_recursive(s, 0, [], result)
    return result


def generate_permutations_recursive(s, index, currPre, result):
    if index == len(s):
        result.append(currPre)
    else:
        for num in range(len(currPre) + 1):
            newPer = list(currPre)
            newPer.insert(num, s[index])
            generate_permutations_recursive(s, index + 1, newPer, result)


print(generate_permutations("AAA"))
