def search_in_2D(matrix, target):
    m, n = len(matrix), len(matrix[0])
    start, end, left, right = 0, m - 1, 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2

        if target <= matrix[mid][0]:
            end = mid - 1
            continue
        start = mid + 1

    if start < m and matrix[start][0] == target:
        return True
    start -= 1

    while left <= right:
        mid_1 = left + (right - left) // 2

        if target <= matrix[start][mid_1]:
            right = mid_1 - 1
            continue
        left = mid_1 + 1

    return left < n and target == matrix[start][left]


print(search_in_2D([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(search_in_2D([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(search_in_2D([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 30))
