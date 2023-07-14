def pairOfSongs(time):
    # timeCount = 0
    # for i in range(len(time)):
    #     for j in range(i,i+1):
    #         if (time[i] + time[j]) % 60 == 0:
    #             timeCount += 1
    # return timeCount

    timeCount = 0
    freq = [0] * 60

    for t in time:
        timeSum = (60 - t % 60) % 60
        timeCount += freq[timeSum]
        freq[t % 60] += 1
    return timeCount


print(pairOfSongs([30, 20, 150, 100, 40]))
print(pairOfSongs([60, 60, 60]))
print(pairOfSongs([20, 40]))
