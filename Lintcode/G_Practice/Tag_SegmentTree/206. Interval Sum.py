"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    class SegTreeNode:
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.sum = 0
            self.left = self.right = None

    """
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """
    def intervalSum(self, A, queries):
        root = self.buildTree(A, 0, len(A) - 1)
        return [self.query(root, q.start, q.end) for q in queries]


    def buildTree(self, arr, start, end):
        if start > end:
            return None

        root = self.SegTreeNode(start, end)

        if start == end:
            root.sum = arr[start]
        else:
            mid = start + (end - start) // 2
            root.left = self.buildTree(arr, start, mid)
            root.right = self.buildTree(arr, mid + 1, end)
            root.sum = root.left.sum + root.right.sum

        return root


    def query(self, root, start, end):
        if not root or start > end or start > root.end or end < root.start:
            return 0

        if start <= root.start and root.end <= end:
            return root.sum

        return self.query(root.left, start, end) + self.query(root.right, start, end)

