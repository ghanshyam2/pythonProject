def fun(lis, char):
    result = ""
    for i in lis:
        if i == " ":
            result += char
        else:
            result += i
    return result


print(fun("aaab ", "c"))
