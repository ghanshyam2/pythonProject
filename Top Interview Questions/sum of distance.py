from collections import defaultdict


def sumOfDistance(nums):
    memo = defaultdict(list)
    for i, n in enumerate(nums):
        memo[n].append(i)

    for k, v in memo.items():
        left_sum = 0
        left_cnt = 0
        right_sum = sum(v)
        right_cnt = len(v)
        for i, idx in enumerate(v):
            right_sum -= idx
            right_cnt -= 1
            nums[idx] = right_sum - idx * right_cnt + idx * left_cnt - left_sum
            left_cnt += 1
            left_sum += idx
    return nums


print(sumOfDistance([1, 3, 1, 1, 2]))
