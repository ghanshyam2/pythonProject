class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.treeDiameter = 0

    def diameter(self, treeRoot):
        self.height_of_tree(treeRoot)
        return self.treeDiameter

    def height_of_tree(self, currNode):
        if currNode is None:
            return 0

        leftRoot = self.height_of_tree(currNode.left)
        rightRoot = self.height_of_tree(currNode.right)
        diam = leftRoot + rightRoot + 1
        self.treeDiameter = max(self.treeDiameter, diam)

        return max(leftRoot, rightRoot) + 1


treeDiam = Tree()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
print(treeDiam.diameter(root))


