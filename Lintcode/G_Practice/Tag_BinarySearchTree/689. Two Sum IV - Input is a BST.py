"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        if not root:
            return None

        l_node = root
        r_node = root
        while l_node.left:
            l_node = l_node.left
        while r_node.right:
            r_node = r_node.right

        while l_node is not r_node:
            summ = l_node.val + r_node.val
            if summ == n:
                return [l_node.val, r_node.val]
            elif summ < n:
                l_node = self.findSuccessor(root, l_node)
            else:
                r_node = self.findPredecessor(root, r_node)

        return None


    def findPredecessor(self, root, target):
        predecessor = None
        node = root
        while node:
            if node is target:
                break
            elif node.val > target.val:
                node = node.left
            else:
                predecessor = node
                node = node.right

        if not node:
            return None

        if not node.left:
            return predecessor

        node = node.left
        while node.right:
            node = node.right

        return node


    def findSuccessor(self, root, target):
        successor = None
        node = root
        while node:
            if node is target:
                break
            elif node.val < target.val:
                node = node.right
            else:
                successor = node
                node = node.left

        if not node:
            return None

        if not node.right:
            return successor

        node = node.right
        while node.left:
            node = node.left

        return node
