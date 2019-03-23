"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        dummy = RandomListNode(0)
        mapping = {}

        new_node = dummy
        old_node = head
        while old_node is not None:
            new_node.next = RandomListNode(old_node.label)
            new_node = new_node.next
            mapping[old_node] = new_node
            old_node = old_node.next

        new_node = dummy.next
        old_node = head
        while old_node is not None:
            if old_node.random:
                new_node.random = mapping[old_node.random]
            old_node = old_node.next
            new_node = new_node.next

        return dummy.next