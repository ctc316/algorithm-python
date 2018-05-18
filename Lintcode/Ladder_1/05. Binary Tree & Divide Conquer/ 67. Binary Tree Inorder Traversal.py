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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        results = []
        self.traverse(root, results)
        return results


    def traverse(self, node, results):
        if node is None:
            return

        self.traverse(node.left, results)
        results.append(node.val)
        self.traverse(node.right)



 # Version 2: Non-Recursive
 class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        if root is None:
            return []

        stack = []
        results = []
        curr = root

        while curr is not None or len(stack) > 0:
            # push all left side childs
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            # handle node
            curr = stack.pop()
            results.append(curr.val)

            # move to right child, or become None
            curr = curr.right

        return results
