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
    @return: the minimum difference between the values of any two different nodes in the tree
    """
    def minDiffInBST(self, root):
        self.minDiff = float("Inf")
        self.cur = None
        self.inorderTraverse(root)
        return self.minDiff


    def inorderTraverse(self, root):
        if not root:
            return

        self.inorderTraverse(root.left)

        if self.cur is not None:
            self.minDiff = min(self.minDiff, abs(root.val - self.cur))
        self.cur = root.val

        self.inorderTraverse(root.right)