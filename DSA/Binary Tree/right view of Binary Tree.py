from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def right_view_of_BTree(root):
    res = []
    if not root:
        return []
    queue = deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0:
                res.append(node.data)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
    return res


root = Node(50)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(15)
root.right.right= Node(35)
root.left.right = Node(25)
print(right_view_of_BTree(root))
