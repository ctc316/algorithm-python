"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        new_node = ListNode(x)
        if not node:
            new_node.next = new_node
            return new_node

        first_node = None
        largest_node = node
        while True:
            if node is first_node:
                new_node.next = largest_node.next
                largest_node.next = new_node
                break
            if first_node is None:
                first_node = node
            if node.val <= new_node.val <= node.next.val:
                new_node.next = node.next
                node.next = new_node
                break
            if node.val > largest_node.val:
                largest_node = node
            node = node.next

        return new_node