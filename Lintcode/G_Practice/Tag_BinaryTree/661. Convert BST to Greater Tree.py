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
    @return: the new root
    """
    def convertBST(self, root):
        self.cur_sum = 0
        self.reversedInorderTraverse(root)
        return root


    def reversedInorderTraverse(self, root):
        if not root:
            return

        self.reversedInorderTraverse(root.right)

        self.cur_sum += root.val
        root.val = self.cur_sum

        self.reversedInorderTraverse(root.left)