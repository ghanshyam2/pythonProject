def bottomView(tree):
    ans = []
    if root is None:
        return ans

    map = defaultdict(int)
    q = deque()
    root.hd = 0
    q.append(root)

    while q:
        temp = q.popleft()
        hd = temp.hd
        map[hd] = temp.data

        if temp.left:
            temp.left.hd = hd - 1
            q.append(temp.left)

        if temp.right:
            temp.right.hd = hd + 1
            q.append(temp.right)

    for value in sorted(map):
        ans.append(map[value])

    return ans