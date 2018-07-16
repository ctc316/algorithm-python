"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# Version 1: Divide and Conquer (DFS), Time: O(n)
class Solution:

    theMin = sys.maxsize

    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if root is None:
            return 0

        self.theMin = sys.maxsize
        self.dfs(root, 0)

        return self.theMin

    def dfs(self, node, depth):
        depth += 1
        if depth >= sys.maxsize:
            return

        if node.left is None and node.right is None:
            if depth < self.theMin:
                self.theMin = depth
        else:
            if node.left is not None:
                self.dfs(node.left, depth)
            if node.right is not None:
                self.dfs(node.right, depth)



# Version 2: Level Order Traveral (BFS), Time: O(n)
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if root is None:
            return 0
        
        from queue import Queue
        q = Queue()
        q.put(root)

        depth = 0
        ans = sys.maxsize
        
        while not q.empty():
            depth += 1
            for i in range(q.qsize()):
                node = q.get()
                if node.left is None and node.right is None and depth < ans:
                    ans = depth
                
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            
        return ans
