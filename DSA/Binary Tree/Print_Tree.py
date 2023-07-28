class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printTree(root):
    if root is None:
        return
    if root.left is not None:
        print("L", root.left.data, end='')
    if root.right is not None:
        print("R", root.right.data, end='')
    print()
    printTree(root.left)
    printTree(root.right)


def inputTree():
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    left = inputTree()
    right = inputTree()
    root.left = left
    root.right = right
    return root


def countNode(root):
    if not root:
        return 0
    return 1 + countNode(root.left) + countNode(root.right)


def maxiMumInBT(root):
    key = 0
    while root:
        if key < root.data:
            key = root.data
        maxiMumInBT(root.left)
        maxiMumInBT(root.right)
    return key


root = inputTree()
printTree(root)
print(countNode(root))
print(maxiMumInBT(root))
