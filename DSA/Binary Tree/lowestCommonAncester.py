class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LCA(root, n1, n2):
    if not root:
        return root

    lca = LCA(root.left, n1, n2)
    rca = LCA(root.right, n1, n2)

    if (lca and rca) and root in [n1, n2]:
        return root
    else:
        return lca or rca


root = Node(50)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(15)
root.left.right = Node(25)
print(LCA(root, 15, 25))
