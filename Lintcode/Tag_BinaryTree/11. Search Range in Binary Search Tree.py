"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        result = []
        self.traverse(root, k1, k2, result)
        return result

    def traverse(self, root, k1, k2, result):
        if not root:
            return

        if root.val >= k1:
            self.traverse(root.left, k1, k2, result)
            if root.val <= k2:
                result.append(root.val)

        if root.val <= k2:
            self.traverse(root.right, k1, k2, result)