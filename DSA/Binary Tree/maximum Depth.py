from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maximumDepth(treeRoot):
    queue = deque([treeRoot])

    maxDepth = 0
    while queue:
        maxDepth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return maxDepth


root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
root.right.right.left = Node(11)
print(maximumDepth(root))
