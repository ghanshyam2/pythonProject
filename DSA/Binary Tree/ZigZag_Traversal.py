from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def zigZagTraversal(treeRoot):
    result = deque()
    answer = []
    if not treeRoot:
        return []
    queue = deque([treeRoot])
    leftToRight = True
    while queue:
        currLevel = deque()
        for _ in range(len(queue)):
            curr_node = queue.popleft()

            if leftToRight:
                currLevel.append(curr_node.data)
            else:
                currLevel.append(curr_node.data)

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        leftToRight = not leftToRight
        # result.appendleft(list(currLevel))
        answer.append(list(currLevel))
    return answer


root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
root.right.right.left = Node(11)
print(zigZagTraversal(root))
