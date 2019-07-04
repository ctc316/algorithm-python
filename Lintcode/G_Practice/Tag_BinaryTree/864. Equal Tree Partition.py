"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """
    def checkEqualTree(self, root):
        if not root:
            return False

        total_sum = self.getSum(root)
        if total_sum % 2 == 1:
            return False
        half_sum = total_sum // 2
        return self.findSum(root.left, half_sum)[0] or self.findSum(root.right, half_sum)[0]


    def getSum(self, root):
        if not root:
            return 0
        return root.val + self.getSum(root.left) + self.getSum(root.right)


    def findSum(self, root, target):
        if not root:
            return False, 0

        l_found, l_sum = self.findSum(root.left, target)
        r_found, r_sum = self.findSum(root.right, target)
        summ = root.val + l_sum + r_sum
        return l_found or r_found or summ == target, summ