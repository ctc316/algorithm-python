"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""

# Version 1: DFS
class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        if root is None:
            return []

        nodes = self.inorderTraverse(root)

        results = []
        for node in nodes:
            self.dfs(None, node, target, [], results)

        return results


    def dfs(self, prev, node, target, combination, results):
        target -= node.val
        combination.append(node.val)

        if target == 0:
            results.append(combination[:])

        if node.left and node.left is not prev:
            self.dfs(node, node.left, target, combination, results)

        if node.right and node.right is not prev:
            self.dfs(node, node.right, target, combination, results)

        if node.parent and node.parent is not prev:
            self.dfs(node, node.parent, target, combination, results)

        combination.pop()


    def inorderTraverse(self, root):
        nodes = []
        stack = []
        curr = root

        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            nodes.append(curr)

            curr = curr.right

        return nodes


# Version 2: 減少函數
class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        results = []
        
        # inorder traverse
        stack = []
        curr = root
        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left

            # for each node, do dfs to find all valid paths
            curr = stack.pop()
            self.dfs(None, curr, target, [], results)

            curr = curr.right

        return results


    def dfs(self, prev, node, target, combination, results):
        target -= node.val
        combination.append(node.val)

        if target == 0:
            results.append(combination[:])

        if node.left and node.left is not prev:
            self.dfs(node, node.left, target, combination, results)

        if node.right and node.right is not prev:
            self.dfs(node, node.right, target, combination, results)

        if node.parent and node.parent is not prev:
            self.dfs(node, node.parent, target, combination, results)

        combination.pop()