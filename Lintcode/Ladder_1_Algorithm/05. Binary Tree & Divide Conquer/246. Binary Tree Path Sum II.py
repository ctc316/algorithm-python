"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Version 1
class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        results = []
        self.preorderTraverse(root, [], 0, results, target)
        return results

    def preorderTraverse(self, node, path, sum, results, target):
        if node is None:
            return

        # add curr node and value
        sum += node.val
        path.append(node.val)
        if sum == target:
            results.append(path[:])

        # deduction from start ot end
        s = sum
        for i in range(len(path) - 1):
            s -= path[i]
            if s == target:
                results.append(path[i + 1 : len(path)])

        self.preorderTraverse(node.left, path, sum, results, target)
        self.preorderTraverse(node.right, path, sum, results, target)

        # backtrace
        del path[len(path) - 1]



# Version 2: 
class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        results = []
        self.preorderTraverse(root, [], results, target)
        return results
    
    def preorderTraverse(self, node, path, results, target):
        if node is None:
            return
        
        path.append(node.val)
        
        # deduction from start ot end
        tmp = target
        for i in range(len(path) - 1, -1, -1):
            tmp -= path[i]
            if tmp == 0:
                results.append(path[i:])
                
        self.preorderTraverse(node.left, path, results, target)
        self.preorderTraverse(node.right, path, results, target)
        
        # backtrace
        path.pop()