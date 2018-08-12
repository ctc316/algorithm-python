"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

# Version 1
class Solution:
    """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        if start <= root.start and root.end <= end:
            return root.max

        result = -sys.maxsize - 1
        mid = root.start + int((root.end -root.start) / 2)
        if mid >= start:  #如果查詢區間和左邊節點區間有交集，則尋找查詢區間在左邊區間上的最大值
            result = max(result, self.query(root.left, start, end))
        if mid + 1 <= end:
            result = max(result, self.query(root.right, start, end))

        return result



# Version 2
class Solution:
    """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        if start > end or root is None or \
           root.start > end or root.end < start:
            return -sys.maxsize - 1

        if start <= root.start and root.end <= end:
            return root.max

        return max(self.query(root.left, start, end), self.query(root.right, start, end))
