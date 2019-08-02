"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, sum):
        results = []
        self.dfs(root, [], sum, results)
        return results


    def dfs(self, root, path, remain, results):
        if not root or remain < 0 :
            return

        remain -= root.val
        path.append(root.val)

        if not root.left and not root.right and remain == 0:
            results.append([p for p in path])
        else:
            self.dfs(root.left, path, remain, results)
            self.dfs(root.right, path, remain, results)

        path.pop()
