class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LCA(treeRoot, n1, n2):
    if not treeRoot:
        return treeRoot

    lca = LCA(treeRoot.left, n1, n2)
    rca = LCA(treeRoot.right, n1, n2)

    if (lca and rca) and treeRoot in [n1, n2]:
        return treeRoot
    else:
        return lca or rca


root = Node(50)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(15)
root.left.right = Node(25)
print(LCA(root, 15, 25))
