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
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        longest, _, _, = self.recursion(root)
        return longest

    def recursion(self, root):
        if root is None:
            return 0, 0, 0

        left_len, left_desc, left_asc = self.recursion(root.left)
        right_len, right_desc, right_asc = self.recursion(root.right)

        descend, ascend = 0, 0

        if root.left is not None:
            if root.left.val == root.val - 1:
                descend = max(descend, left_desc + 1)

            elif root.left.val == root.val + 1:
                ascend = max(ascend, left_asc + 1)

        if root.right is not None:
            if root.right.val == root.val - 1:
                descend = max(descend, right_desc + 1)

            elif root.right.val == root.val + 1:
                ascend = max(ascend, right_asc + 1)

        leng = descend + 1 + ascend
        longest = max(leng, left_len, right_len)

        return longest, descend, ascend