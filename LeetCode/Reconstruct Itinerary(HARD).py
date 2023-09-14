from collections import defaultdict


def reconstruct(tickets):
    graph = defaultdict(list)
    for f, t in sorted(tickets, reverse=True):
        graph[f].append(t)

    result = []

    def travel(node):
        while graph[node]:
            nextNode = graph[node].pop()
            travel(nextNode)

        result.append(node)

    travel("JFK")

    return result[::-1]


print(reconstruct([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
