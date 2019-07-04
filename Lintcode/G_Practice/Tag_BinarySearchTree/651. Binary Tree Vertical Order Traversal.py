"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        if not root:
            return []

        records = {}
        from queue import Queue
        q = Queue()
        q.put((root, 0))
        while not q.empty():
            node, idx = q.get()
            if idx not in records:
                records[idx] = []
            records[idx].append(node.val)
            if node.left:
                q.put((node.left, idx - 1))
            if node.right:
                q.put((node.right, idx + 1))

        return [records[k] for k in sorted(records.keys())]