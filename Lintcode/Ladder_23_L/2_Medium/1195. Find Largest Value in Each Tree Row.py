"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of integer
    @return: return a list of integer
    """
    def largestValues(self, root):
        if root is None:
            return []

        from queue import Queue
        q = Queue()
        q.put(root)

        results = []
        while not q.empty():
            largest = -sys.maxsize - 1
            for _ in range(q.qsize()):
                node = q.get()
                largest = max(node.val, largest)

                if node.left is not None:
                    q.put(node.left)

                if node.right is not None:
                    q.put(node.right)

            results.append(largest)

        return results