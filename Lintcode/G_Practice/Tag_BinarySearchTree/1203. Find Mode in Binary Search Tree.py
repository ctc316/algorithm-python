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
    @return: return a integer
    """
    def findMode(self, root):
        self.count = 0
        self.max_count = 0
        self.modes = []
        self.cur = None
        self.prev = None
        self.inorderTraverse(root)

        if self.cur is not None:
            if self.count > self.max_count:
                self.modes = [self.cur]
            elif self.count == self.max_count:
                self.modes.append(self.cur)

        return self.modes


    def inorderTraverse(self, root):
        if not root:
            return

        self.inorderTraverse(root.left)

        self.prev = self.cur
        self.cur = root.val
        if self.prev is not None and self.cur != self.prev:
            if self.count > self.max_count:
                self.modes = [self.prev]
            elif self.count == self.max_count:
                self.modes.append(self.prev)
            self.max_count = max(self.max_count,  self.count)
            self.count = 0

        self.count += 1

        self.inorderTraverse(root.right)