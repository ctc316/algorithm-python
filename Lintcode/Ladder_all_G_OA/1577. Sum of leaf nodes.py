"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root:
    @return: the sum of leafnode
    """
    def sumLeafNode(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.val

        return self.sumLeafNode(root.left) + self.sumLeafNode(root.right)