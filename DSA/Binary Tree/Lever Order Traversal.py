from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelOrderTraversal(treeRoot):
    res = []
    if not treeRoot:
        return []
    queue = deque([treeRoot])
    while queue:
        node = []
        for _ in range(len(queue)):
            curr_node = queue.popleft()
            node.append(curr_node.data)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        res.append(node)
    return res


root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print(levelOrderTraversal(root))
