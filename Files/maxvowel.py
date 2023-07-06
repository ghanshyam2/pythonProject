def maxVowel(S):
    vowel = "AEIOU"
    count = temp = 0
    for i in range(len(S)):
        if S[i] in vowel:
            count += 1
            if count > temp:
                temp += 1
        else:
            count = 0
    return temp


print(maxVowel("ASIEOMAXGETLOSTPOP"))
print(maxVowel("ABCDAESPIODU"))
print(maxVowel("PSDPKLTYRFGH"))
