def changeTrafficLights(S, K):
    m = len(S)
    count = 0
    lis = ""
    for i in range(m):
        if count <= K:
            if S[i] == "R":
                lis += "B"
            if S[i] == "B":
                lis += "G"
            if S[i] == "G":
                lis += "R"
        else:
            lis += "R"
        count += 1
    return lis


# K is denotes traffic lights changed every K minutes.
print(changeTrafficLights("RBRG", 2))
print(changeTrafficLights("RRBGR", 5))
