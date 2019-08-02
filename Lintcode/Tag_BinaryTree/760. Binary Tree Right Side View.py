"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    def rightSideView(self, root):
        if not root:
            return []
            
        from queue import Queue
        q = Queue()
        q.put(root)
        result = []
        
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                
                if i == size - 1:
                    result.append(node.val)
        
        return result
                