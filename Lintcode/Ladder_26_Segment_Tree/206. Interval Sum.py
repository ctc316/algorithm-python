"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class SegTreeNode:
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, arr):
        self.root = self._build(arr, 0, len(arr) - 1)


    def _build(self, arr, start, end):
        if start > end:
            return None

        if start == end:
            return SegTreeNode(start, end, arr[start])

        mid = start + int((end - start) / 2)
        root = SegTreeNode(start, end, 0)
        root.left = self._build(arr, start, mid)
        root.right = self._build(arr, mid + 1, end)

        if root.left:
            root.sum += root.left.sum
        if root.right:
            root.sum += root.right.sum

        return root


    def query(self, start, end):
        return self._query(self.root, start, end)


    def _query(self, root, start, end):
        if root is None or root.end < start or root.start > end:
            return 0

        if start <= root.start and root.end <= end:
            return root.sum

        return self._query(root.left, start, end) + self._query(root.right, start, end)


class Solution:
    """
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """
    def intervalSum(self, A, queries):
        seg_tree = SegmentTree(A)
        results = []
        for q in queries:
            results.append(seg_tree.query(q.start, q.end))

        return results