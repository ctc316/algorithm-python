"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Version 1: Recursive
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        results = []
        self.traverse(root, results)
        return results


    def traverse(self, node, results):
        if node is None:
            return

        results.append(node.val)
        self.traverse(node.left, results)
        self.traverse(node.right, results)


# Version 2: Non-Recursive
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if root is None:
            return []

        stack = []
        results = []

        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            results.append(node.val)

            # put the right child to stack first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return results