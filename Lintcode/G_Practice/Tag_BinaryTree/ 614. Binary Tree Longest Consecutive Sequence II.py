'''
Given a binary tree, find the length(number of nodes) of the longest consecutive sequence path.
The path could be start and end at any node in the tree

Example 1:

Input:
{1,2,0,3}
Output:
4
Explanation:
    1
   / \
  2   0
 /
3
0-1-2-3


Example 2:

Input:
{3,2,2}
Output:
2
Explanation:
    3
   / \
  2   2
2-3
'''


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
        longest, _, _ = self.helper(root)
        return longest


    def helper(self, root):
        if not root:
            return 0, 0, 0

        l_longest, l_asd, l_dsc  = self.helper(root.left)
        r_longest, r_asd, r_dsc = self.helper(root.right)

        asd = 0
        dsc = 0
        if root.left:
            if root.val == root.left.val + 1:
                dsc = max(dsc, l_dsc)
            elif root.val == root.left.val - 1:
                asd = max(asd, l_asd)
        if root.right:
            if root.val == root.right.val + 1:
                dsc = max(dsc, r_dsc)
            elif root.val == root.right.val - 1:
                asd = max(asd, r_asd)

        return max(l_longest, r_longest, asd + dsc + 1), asd + 1, dsc + 1