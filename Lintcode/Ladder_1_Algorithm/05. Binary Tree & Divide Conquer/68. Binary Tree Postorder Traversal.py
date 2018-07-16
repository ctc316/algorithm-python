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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        results = []
        self.traverse(root, results)
        return results

    def traverse(self, root, results):
        if root is None:
            return

        self.traverse(root.left, results)
        self.traverse(root.right, results)
        results.append(root.val)



# Version 2: Non-Recursive
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        if root is None:
            return []
        
        results = []    
        stack = []
        prev = None 
        curr = root
        
        stack.append(root)
        
        while len(stack) > 0:
            curr = stack[-1]  # peek()
            if prev is None or prev.left is curr or prev.right is curr:
                # traverse down the tree
                if curr.left is not None:
                    stack.append(curr.left)
                elif curr.right is not None:
                    stack.append(curr.right)
                    
            elif curr.left is prev:
                # traverse up the tree from the left
                if curr.right is not None:
                    stack.append(curr.right)
            else:
                results.append(curr.val)
                stack.pop()
            
            prev = curr
            
        return results