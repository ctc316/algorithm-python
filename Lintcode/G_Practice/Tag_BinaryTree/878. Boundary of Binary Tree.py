'''
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.


Example 1:

Input: {1,#,2,3,4}
Output: [1,3,4,2]
Explanation:
  1
   \
    2
   / \
  3   4
  The root doesn't have left subtree, so the root itself is left boundary.
  The leaves are node 3 and 4.
  The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
  So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Example 2:

Input: {1,2,3,4,5,6,#,#,#,7,8,9,10}
Output: [1,2,4,7,8,9,10,6,3]
Explanation:
          1
     /          \
    2            3
   / \          /
  4   5        6
     / \      / \
    7   8    9  10
  The left boundary are node 1,2,4. (4 is the left-most node according to definition)
  The leaves are node 4,7,8,9,10.
  The right boundary are node 1,3,6,10. (10 is the right-most node).
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
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []

        self.left_bound = []
        self.right_bound = []
        self.leaves = []

        self.helper(root.left, True, False)
        self.helper(root.right, False, True)

        res = [root.val]
        res.extend(self.left_bound)
        res.extend(self.leaves)
        res.extend(reversed(self.right_bound))
        return res


    def helper(self, root, is_left_bound, is_right_bound):
        if not root:
            return

        if not root.left and not root.right:
            self.leaves.append(root.val)
            return

        if is_left_bound:
            self.left_bound.append(root.val)
        elif is_right_bound:
            self.right_bound.append(root.val)

        self.helper(root.left, is_left_bound,  is_right_bound and not root.right)
        self.helper(root.right, is_left_bound and not root.left, is_right_bound)

