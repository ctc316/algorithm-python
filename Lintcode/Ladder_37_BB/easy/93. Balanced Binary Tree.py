"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        isBal, _ = self.helper(root)
        return isBal


    def helper(self, root):
        if not root:
            return True, 0

        l_isBal, l_cnt = self.helper(root.left)
        r_isBal, r_cnt = self.helper(root.right)

        return l_isBal and r_isBal and abs(l_cnt - r_cnt) < 2, max(l_cnt, r_cnt) + 1