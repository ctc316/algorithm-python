"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        if not nums or len(nums) == 0:
            return None
            
        max_num = 0
        max_idx = 0
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_idx = i
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])
        return root