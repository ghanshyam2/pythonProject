def eventualSafe(graph):
    n = len(graph)
    safe = {}

    def dfs(i):
        if i in safe:
            return safe[i]
        safe[i] = False
        for nei in graph[i]:
            if not dfs(nei):
                return safe[i]
        safe[i] = True
        return safe[i]

    result = []
    for i in range(n):
        if dfs(i):
            result.append(i)
    return result


print(eventualSafe([[1, 2], [2, 3], [5], [0], [5], [], []]))
print(eventualSafe([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
