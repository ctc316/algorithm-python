"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the minimum absolute difference between values of any two nodes
    """
    def getMinimumDifference(self, root):
        self.minDiff = float("Inf")
        self.prev = None
        self.inorderTraverse(root)
        return self.minDiff

    def inorderTraverse(self, root):
        if not root:
            return

        self.inorderTraverse(root.left)

        if self.prev is not None:
            self.minDiff = min(self.minDiff, abs(root.val - self.prev))
        self.prev = root.val

        self.inorderTraverse(root.right)