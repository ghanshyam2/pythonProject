def trappingRainWater(height):
    left = res = 0
    right = len(height) - 1
    leftM = rightM = 0
    n = len(height)
    if n == 0:
        return 0
    while left < right:
        if height[left] < height[right]:
            if height[left] > leftM:
                leftM = height[left]
            else:
                res += leftM - height[left]
            left += 1
        else:
            if height[right] > rightM:
                rightM = height[right]
            else:
                res += rightM - height[right]
            right -= 1
    return res


print(trappingRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
