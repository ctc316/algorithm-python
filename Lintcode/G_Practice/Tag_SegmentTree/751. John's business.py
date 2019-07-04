class SegTreeNode:
    def __init__(self, start, end, min):
        self.start = start
        self.end = end
        self.min = min
        self.left = None
        self.right = None

class SegTree:
    def __init__(self, arr):
        self.root = self.__buildTree(arr, 0, len(arr) - 1)


    def __buildTree(self, arr, start, end):
        if start > end:
            return None

        root = SegTreeNode(start, end, arr[end])

        if start == end:
            return root

        mid = start + (end - start) // 2
        root.left = self.__buildTree(arr, start, mid)
        root.right = self.__buildTree(arr, mid + 1, end)
        root.min = min(root.left.min, root.right.min)

        return root


    def query(self, start, end):
        return self.__queryHelper(self.root, start, end)


    def __queryHelper(self, root, start, end):
        if not root or start > end or root.start > end or root.end < start:
            return float("Inf")

        if start <= root.start and root.end <= end:
            return root.min

        return min(self.__queryHelper(root.left, start, end),
                   self.__queryHelper(root.right, start, end))


class Solution:
    """
    @param A: The prices [i]
    @param k:
    @return: The ans array
    """
    def business(self, A, k):
        n = len(A)
        sgTree = SegTree(A)
        res = [0 for _ in A]
        for i in range(n):
            mini = sgTree.query(max(0, i - k), min(n - 1, i + k))
            if A[i] > mini:
                res[i] = A[i] - mini

        return res
