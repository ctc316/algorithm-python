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
    @return: An integer
    """
    def maxPathSum(self, root):
        maxSum, _ = self.recursion(root)
        return maxSum

    def recursion(self, root):
        if root is None:
            return 0, 0

        left_max = right_max = -sys.maxsize - 1
        left_sum = right_sum = 0

        if root.left:
            left_max, left_sum = self.recursion(root.left)
            left_sum = max(0, left_sum)

        if root.right:
            right_max, right_sum = self.recursion(root.right)
            right_sum = max(0, right_sum)

        combined_max = left_sum + root.val + right_sum
        retSum = root.val + max(left_sum, right_sum)

        return max(left_max, right_max, combined_max), retSum