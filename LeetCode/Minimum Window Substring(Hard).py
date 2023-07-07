def Min_window_subString(s, t):
    wind_start, matched, sub_str = 0, 0, 0
    min_len = len(s) + 1
    char_frq = {}

    for ch in t:
        if ch not in char_frq:
            char_frq[ch] = 0
        char_frq[ch] += 1

    for wind_end in range(len(s)):
        right_chr = s[wind_end]
        if right_chr in char_frq:
            char_frq[right_chr] -= 1
            if char_frq[right_chr] >= 0:
                matched += 1
        while matched == len(t):
            if min_len > wind_end - wind_start + 1:
                min_len = wind_end - wind_start + 1
                sub_str = wind_start
            left_chr = s[wind_start]
            wind_start += 1
            if left_chr in char_frq:
                if char_frq[left_chr] == 0:
                    matched -= 1
                char_frq[left_chr] += 1
    if min_len > len(s):
        return "No String"
    return s[sub_str:sub_str + min_len]


print(Min_window_subString("abcad", "abc"))
print(Min_window_subString("aabdec", "abc"))
print(Min_window_subString("adcad", "abc"))
print(Min_window_subString("ADOBECODEBANC", "ABC"))
print(Min_window_subString("a", "a"))
print(Min_window_subString("a", "aa"))
