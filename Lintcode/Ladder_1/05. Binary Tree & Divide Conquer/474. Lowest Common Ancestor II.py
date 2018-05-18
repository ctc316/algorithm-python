"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""

# Version 1: Postorder Traverse
'''
思路：Postorder Traverse
從底部開始遍歷，並將可能的答案節點向上傳遞。
情況1：遇到本身為答案，回傳自己
情況2：遇到左右子樹皆為答案，回傳自己
情況3：遇到其中一子樹為答案，將子樹結果往上傳
情況4：當兩子樹都無答案，回傳 None

時間複雜度：O(n)
空間複雜度：O(1)
'''
class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        if root is None:
            return None

        # found an answer node or it can possibly be the LCA node
        if root is A or root is B:
            return root

        left = self.lowestCommonAncestorII(root.left, A, B)
        right = self.lowestCommonAncestorII(root.right, A, B)

        # when left and right are both answers, the node is LCA
        if (left is A or left is B) and (right is A or right is B):
            return root

        # pick a side that is not None if available
        if left is not None:
            return left
        return right


# Version 2: 從 A, B 向上遍歷
class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        dict = {}
        while A is not None:
            dict[A] = True
            A = A.parent

        while B is not None:
            if B in dict:
                return B
            B = B.parent

        return root