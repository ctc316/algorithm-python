# Version 1: Naive, Time: O(n^2), TLE
class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        n = len(A)
        results = [0 for _ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if A[i] < A[j]:
                    results[j] += 1

        return results


# Version 2: Segment Tree, Time: O(n * 10000)
class SegTreeNode:
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, start, end):
        self.root = self._build(start, end)


    def _build(self, start, end):
        if start > end:
            return None

        if start == end:
            return SegTreeNode(start, end, 0)

        mid = start + int((end - start) / 2)
        root = SegTreeNode(start, end, 0)
        root.left = self._build(start, mid)
        root.right = self._build(mid + 1, end)

        return root


    def query(self, start, end):
        return self._query(self.root, start, end)


    def _query(self, root, start, end):
        if root is None or root.end < start or root.start > end:
            return 0

        if start <= root.start and root.end <= end:
            return root.count

        return self._query(root.left, start, end) + self._query(root.right, start, end)


    def increase(self, index):
        self._increase(self.root, index)


    def _increase(self, root, index):
        if root.start == root.end:
            root.count += 1
            return

        if index <= root.left.end:
            self._increase(root.left, index)
        else:
            self._increase(root.right, index)

        root.count = root.left.count + root.right.count


class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        if len(A) == 0:
            return []

        seg_tree = SegmentTree(0, max(A))
        results = []
        for a in A:
            results.append(seg_tree.query(0, a - 1))
            seg_tree.increase(a)

        return results