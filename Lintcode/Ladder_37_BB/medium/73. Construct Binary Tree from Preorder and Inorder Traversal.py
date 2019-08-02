"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, preorder, inorder):
        '''
        pre:  [2,1,4,5,3,7]
        in:   [4,1,5,2,3,7]

              2
          1      3
        4   5      7
        '''
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        root_idx = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:root_idx + 1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])

        return root