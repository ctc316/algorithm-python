"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:

    longest = 0

    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        self.longest = 0
        self.dfs(root, 0, [])
        return self.longest

    def dfs(self, node, length, combination):
        if node is None:
            return

        if length != 0 and node.val != combination[-1] + 1:
            length = 0
            combination = []

        length += 1
        combination.append(node.val)

        if length > self.longest:
            self.longest = length

        if node.left:
            self.dfs(node.left, length, combination)
        if node.right:
            self.dfs(node.right, length, combination)

        combination.pop()