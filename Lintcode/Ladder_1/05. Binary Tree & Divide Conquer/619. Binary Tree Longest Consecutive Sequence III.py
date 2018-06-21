"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""

class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        longest, _, _ = self.recursion(root)
        return longest


    def recursion(self, root):
        if root is None:
            return 0, 0, 0

        descend, ascend = 0, 0
        max_child_len = 0
        
        for child in root.children:
            child_len, child_desc, child_asc = self.recursion(child)

            # max from child
            if child_len > max_child_len:
                max_child_len = child_len

            # find the longest decend
            if child.val == root.val - 1:
                descend = max(descend, child_desc)

            # find the longest ascend
            elif child.val == root.val + 1:
                ascend = max(ascend, child_asc)


        length = descend + 1 + ascend
        longest = max(length, max_child_len)

        return longest, descend + 1, ascend + 1