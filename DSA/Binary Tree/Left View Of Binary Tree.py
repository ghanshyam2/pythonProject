from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0


def left_view_of_BTree(treeRoot):
    result =[]
    if not treeRoot:
        return
    q = [treeRoot]
    while len(q):
        for i in range(1, len(q) + 1):
            temp = q[0]
            q.pop(0)
            if i == 1:
                result.append(temp.data)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
    return result


root = Node(10)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)
print(left_view_of_BTree(root))
root = Node(50)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(15)
root.right.right= Node(35)
root.right.right.left = Node(25)
print(left_view_of_BTree(root))
