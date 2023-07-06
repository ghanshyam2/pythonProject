def next_letter_binary_search(letters, key):
    if letters[0] > key or letters[len(letters) - 1] < key:
        return letters[0]

    left, right = 0, len(letters) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if key < letters[mid]:
            right = mid -1
        else:

            left = mid + 1
    return letters[left % len(letters)]


print(next_letter_binary_search(['a', 'b', 'd', 'f', 'h'], 'f'))
print(next_letter_binary_search(['a','c','d','f','h'], 'b'))
print(next_letter_binary_search(['a','b','d','x','h'],'v'))
