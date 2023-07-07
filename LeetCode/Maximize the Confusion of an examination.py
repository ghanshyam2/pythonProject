import collections


def confusionExam(st, k):
    maxSize = 0
    count = collections.Counter()

    for right in range(len(st)):
        count[st[right]] += 1
        min_count = min(count['T'], count['F'])

        if min_count <= k:
            maxSize += 1
        else:
            count[st[right - maxSize]] -= 1
    return maxSize


print(confusionExam("TFFT", 2))
print(confusionExam('TFFT', 1))
print(confusionExam('TTFTTFTT', 1))
