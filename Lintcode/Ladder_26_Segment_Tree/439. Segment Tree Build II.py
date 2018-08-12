"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, A):
        return self.helper(A, 0, len(A) - 1)


    def helper(self, A, start, end):
        if start > end:
            return None

        root = SegmentTreeNode(start, end, A[end])

        if start == end:
            return root

        mid = start + int((end - start) / 2)
        root.left = self.helper(A, start, mid)
        root.right = self.helper(A, mid + 1, end)
        root.max = max(root.left.max, root.right.max)

        return root