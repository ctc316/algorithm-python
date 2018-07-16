"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        return self.dfs(root)

    def dfs(self, root):
        if root is None:
            return -sys.maxsize - 1

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return max(root.val, root.val + max(left, right))