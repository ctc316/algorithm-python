"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Version 1: Inorder traverse, Time: O(n)
class Solution:

    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        if root is None:
            return None

        prev = None
        curr = root
        stack = []

        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if curr is p:
                return prev

            prev = curr
            curr = curr.right

        return None




# Version 2: BST, O(logn)
class Solution:
    
    prev = None
    
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        if root is None:
            return None
        
        if p.val > root.val:
            self.prev = root
            return self.inorderPredecessor(root.right, p)
            
        elif p.val < root.val:
            return self.inorderPredecessor(root.left, p)
            
        else:
            if root.left:
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                return predecessor
            else:
                return self.prev