"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

#version 1: reverse the layer output
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
            
        results = []
        
        from queue import Queue
        q = Queue()
        q.put(root)
        
        reverse = False
        
        while not q.empty():
            level = []
            for i in range(q.qsize()):
                node = q.get()
                level.append(node.val)
                
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            
            if reverse:
                level.reverse()
            
            results.append(level)
            reverse = not reverse
        
        return results
            
        

#version 2: reverse the queue list
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        results = []

        list = []
        list.append(root)

        reverse = False

        while len(list) > 0:
            level = []
            size = len(list)
            for i in range(size):
                node = list[i]
                level.append(node.val)

                if reverse:
                    if node.right is not None:
                        list.append(node.right)
                    if node.left is not None:
                        list.append(node.left)
                else:
                    if node.left is not None:
                        list.append(node.left)
                    if node.right is not None:
                        list.append(node.right)

            results.append(level)

            list = list[size:]
            list.reverse()

            reverse = not reverse

        return results