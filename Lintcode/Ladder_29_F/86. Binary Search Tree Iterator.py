"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []
        if root:
            self.stack.append(root)

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        root = self.stack.pop()
        if root.left:
            while root:
                self.stack.append(root)
                left = root.left
                root.left = None
                root = left

            root = self.stack.pop()

        if root.right:
            self.stack.append(root.right)

        return root