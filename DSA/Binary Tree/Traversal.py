class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(root):
    lists = []
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)


def preOrder(root):
    if root:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')





root = Node(30)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(15)
root.left.right = Node(25)
inOrder(root)
preOrder(root)
postOrder(root)

print()
