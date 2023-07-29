class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maximumTree(root):
    leftMax = 0
    rightMax = 0
    if not root:
        return root
    leftMax = max(leftMax, root.left.data)
    rightMax = max(rightMax, root.right.data)

    return max(root.data, max(leftMax, rightMax))


def minimumTree(root):
    leftMin = root.data
    rightMin = root.data
    if not root:
        return root
    leftMin = min(leftMin, root.left.data)
    rightMin = min(rightMin, root.right.data)

    return min(root.data, min(leftMin, rightMin))


root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(10)
root.right.right = Node(5)
print(maximumTree(root))
print(minimumTree(root))
