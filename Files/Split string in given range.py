def string_split(string):
    output = [string[i:i + 3] for i in range(0, len(string), 3)]
    return output


print(string_split("ABCDEFGHIJKLMNOP"))
