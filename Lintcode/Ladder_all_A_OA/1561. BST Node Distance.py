class TNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TNode(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, curr, val):
        if val < curr.val:
            if curr.left:
                self.insertNode(curr.left, val)
            else:
                curr.left = TNode(val)
        else:
            if curr.right:
                self.insertNode(curr.right, val)
            else:
                curr.right = TNode(val)


class Solution:
    """
    @param numbers: the given list
    @param node1: the given node1
    @param node2: the given node2
    @return: the distance between two nodes
    """
    def bstDistance(self, numbers, node1, node2):
        bst = BST()
        count = 0
        for num in numbers:
            bst.insert(num)
            if node1 == num or node2 == num:
                count += 1

        if count < 2:
            return -1

        lca = self.lowestCommonAncestor(bst.root, node1, node2)
        return self.calculateDistance(lca, node1) + self.calculateDistance(lca, node2)


    def lowestCommonAncestor(self, root, A, B):
        if root is None or root.val == A or root.val == B:
            return root

        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right


    def calculateDistance(self, root, node):
        if root.val == node:
            return 0
        if node < root.val:
            return self.calculateDistance(root.left, node) + 1
        else:
            return self.calculateDistance(root.right, node) + 1