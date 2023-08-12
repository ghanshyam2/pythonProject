class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def path(treeRoot, sums):
    if treeRoot is None:
        return False

    if treeRoot.data == sums and treeRoot.left is None and treeRoot.right is None:
        return True

    return path(treeRoot.left, sums - treeRoot.data) or path(treeRoot.right, sums - treeRoot.data)


root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print("The Path is :", str(path(root, 23)))
print("The Path is :", str(path(root, 16)))

# Time Complexity = O(N)
# Space Complexity = O(N)
