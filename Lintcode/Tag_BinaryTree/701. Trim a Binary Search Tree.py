"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree
    """
    def trimBST(self, root, minimum, maximum):
        '''
        root < minimum => return root.right
        root > maximum => return root.left
        else =>  root.left <- root.left;  root.right <- root.right; return root
        '''

        if not root:
            return root

        root.right = self.trimBST(root.right, minimum, maximum)
        if root.val < minimum:
            return root.right

        root.left = self.trimBST(root.left, minimum, maximum)
        if root.val > maximum:
            return root.left

        return root


