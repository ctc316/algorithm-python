"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if root is None:
            return []
            
        result = []
        
        from queue import Queue
        q = Queue()
        q.put(root)
        
        while not q.empty():
            size = q.qsize()
            dummy = ListNode(0)
            curr = dummy
            for i in range(size):
                node = q.get()
                curr.next = ListNode(node.val)
                curr = curr.next
                
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
                
            result.append(dummy.next)
            
        return result