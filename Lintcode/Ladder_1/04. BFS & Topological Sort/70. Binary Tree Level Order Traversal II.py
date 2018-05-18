"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        if root is None:
            return []

        results = []

        from queue import Queue
        q = Queue()
        q.put(root)
        
        while not q.empty():
            level = []
            for i in range(q.qsize()):
                node = q.get()
                level.append(node.val)

                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)

            results.insert(0, level)

        return results