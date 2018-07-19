"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        result, _, _ = self.helper(root)
        return result


    def helper(self, root):
        if root is None:
            return root, -sys.maxsize - 1, 0

        l_max_node, l_max, l_sum = self.helper(root.left)
        r_max_node, r_max, r_sum = self.helper(root.right)

        curr_sum = root.val + l_sum + r_sum
        maxi = curr_sum
        maxi_node = root

        if l_max > maxi:
            maxi = l_max
            maxi_node = l_max_node

        if r_max > maxi:
            maxi = r_max
            maxi_node = r_max_node

        return maxi_node, maxi, curr_sum