def min_add_valid_string(word):
    n = len(word)
    i = ins = 0

    while i < n:
        if word[i:i + 3] == 'abc':
            i += 3
        elif word[i:i + 2] == {'ab', 'bc', 'ac'}:
            ins += 1
            i += 2
        else:
            ins += 2
            i += 1
        return ins


print(min_add_valid_string("aaaaab"))
