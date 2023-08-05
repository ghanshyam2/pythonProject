from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def right_view_of_BTree(treeRoot):
    res = []
    if not treeRoot:
        return []
    queue = deque([treeRoot])
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
root.right.right.left = Node(25)
print(right_view_of_BTree(root))
root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
root.right.right.left = Node(3)
print(right_view_of_BTree(root))
