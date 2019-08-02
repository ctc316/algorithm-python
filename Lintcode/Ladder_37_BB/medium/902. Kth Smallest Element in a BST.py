"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        self.idx = 0
        return self.inorderTraverse(root, k)


    def inorderTraverse(self, root, k):
        if root is None:
            return None

        left = self.inorderTraverse(root.left, k)
        if left is not None:
            return left

        self.idx += 1
        if self.idx == k:
            return root.val

        return self.inorderTraverse(root.right, k)