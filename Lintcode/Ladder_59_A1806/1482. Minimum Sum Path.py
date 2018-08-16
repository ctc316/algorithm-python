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
    @return: minimum sum
    """
    def minimumSum(self, root):
        return self.helper(root, 0)


    def helper(self, root, path_sum):
        """
        @param root: root for subtree
        @param path_sum: current path sum
        @return: minimum sum
        """
        if root is None:
            return sys.maxsize

        path_sum += root.val

        if root.left is None and root.right is None:
            return path_sum

        return min(self.helper(root.left, path_sum), self.helper(root.right, path_sum))