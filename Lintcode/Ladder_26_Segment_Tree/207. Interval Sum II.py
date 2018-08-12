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


    def modify(self, index, value):
        self._modify(self.root, index, value)


    def _modify(self, root, index, value):
        if root.start == root.end:
            root.sum = value
            return

        if index <= root.left.end:
            self._modify(root.left, index, value)
        else:
            self._modify(root.right, index, value)

        root.sum = root.left.sum + root.right.sum



class Solution:
    """
    @param: A: An integer array
    """
    def __init__(self, A):
        self.seg_tree = SegmentTree(A)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        return self.seg_tree.query(start, end)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        self.seg_tree.modify(index, value)