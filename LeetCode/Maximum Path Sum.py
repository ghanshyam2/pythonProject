import math


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def max_path_sum(self, root):
        self.globalMaximum = -math.inf
        self.path_sum_recursive(root)
        return self.globalMaximum

    def path_sum_recursive(self, currNode):
        if currNode is None:
            return 0

        currNodeMaxLeft = self.path_sum_recursive(currNode.left)
        currNodeRight = self.path_sum_recursive(currNode.right)

        currNodeMaxLeft = max(currNodeMaxLeft, 0)
        currNodeRight = max(currNodeRight, 0)

        localMaxSum = currNodeMaxLeft + currNodeRight + currNode.val

        self.globalMaximum = max(self.globalMaximum, localMaxSum)
        return max(currNodeMaxLeft, currNodeRight) + currNode.val


