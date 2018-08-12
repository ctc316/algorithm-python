"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class SegTreeNode:
    def __init__(self, start, end, min):
        self.start = start
        self.end = end
        self.min = min
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
        root = SegTreeNode(start, end, sys.maxsize)
        root.left = self._build(arr, start, mid)
        root.right = self._build(arr, mid + 1, end)

        if root.left:
            root.min = min(root.min, root.left.min)
        if root.right:
            root.min = min(root.min, root.right.min)

        return root


    def query(self, start, end):
        return self._query(self.root, start, end)


    def _query(self, root, start, end):
        if root is None or root.end < start or root.start > end:
            return sys.maxsize

        if start <= root.start and root.end <= end:
            return root.min

        return min(self._query(root.left, start, end), self._query(root.right, start, end))



class Solution:
    """
    @param A: An integer array
    @param queries: An query list
    @return: The result list
    """
    def intervalMinNumber(self, A, queries):
        seg_tree = SegmentTree(A)
        results = []
        for q in queries:
            results.append(seg_tree.query(q.start, q.end))

        return results