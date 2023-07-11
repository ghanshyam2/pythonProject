def KthEle(A, n, m, k):
    top = 0
    down = n - 1
    left = 0
    right = m - 1
    direction = 0
    idx = 1

    while top <= down and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                if idx == k:
                    return A[top][i]
                idx += 1
            top += 1
        elif direction == 1:
            for i in range(top, down + 1):
                if idx == k:
                    return A[i][right]
                idx += 1
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                if idx == k:
                    return A[down][i]
                idx += 1
            down -= 1
        else:
            for i in range(down, top - 1, -1):
                if idx == k:
                    return A[i][left]
                idx += 1
            left += 1

        direction = (direction + 1) % 4

    return -1


print(KthEle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4, 4, 10))
