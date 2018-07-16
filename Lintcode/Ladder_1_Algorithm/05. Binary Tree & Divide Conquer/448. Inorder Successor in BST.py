"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


# Version 1: Inorder Traverse
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        foundP = False
        stack = []
        curr = root

        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if foundP is True:
                return curr
            if curr is p:
                foundP = True

            curr = curr.right

        return None


# Version 2: BST
class Solution:

    next = None

    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        if root is None:
            return None

        if root is p:
            if root.right:
                successor = root.right
                while successor.left:
                    successor = successor.left
                return successor
            else:
                return self.next

        if p.val <= root.val:
            self.next = root
            return self.inorderSuccessor(root.left, p)

        if p.val > root.val:
            return self.inorderSuccessor(root.right, p)
