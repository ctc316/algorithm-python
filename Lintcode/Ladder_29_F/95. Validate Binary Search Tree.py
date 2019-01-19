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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        self.cur = -float('Inf')
        return self.inorderTraverse(root)


    def inorderTraverse(self, node):
        if node is None:
            return True

        if not self.inorderTraverse(node.left):
            return False

        if node.val <= self.cur:
            return False

        self.cur = node.val

        if not self.inorderTraverse(node.right):
            return False

        return True