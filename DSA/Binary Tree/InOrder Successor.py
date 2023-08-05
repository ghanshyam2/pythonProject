class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrderSuccessor(root, x):
    arr = [None]
    while root:
        if root.data > x.data:
            arr[0] = root
            root = root.left
        else:
            root = root.right

    return arr[0]


x = int(input())
root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print(inOrderSuccessor(root, Node(x)))
