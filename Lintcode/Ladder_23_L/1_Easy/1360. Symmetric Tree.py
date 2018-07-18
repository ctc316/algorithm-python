"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself
    """
    def isSymmetric(self, root):
        if root is None:
            return True

        from queue import Queue
        q = Queue()
        q.put(root)

        while not q.empty():
            size = q.qsize()
            level = []
            for _ in range(size):
                node = q.get()
                level.append(node)

                if node is not None:
                    q.put(node.left)
                    q.put(node.right)

            # check symmetricity
            left = 0
            right = size - 1
            while left < right:
                if level[left] is None and level[right] is None:
                    left += 1
                    right -= 1
                    continue

                if level[left] is None or level[right] is None or \
                   level[left].val != level[right].val:
                    return False
                left += 1
                right -= 1

        return True