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

        # copy nodes and record mapping
        new_tail = dummy
        old_tail = head
        while old_tail is not None:
            new_tail.next = RandomListNode(old_tail.label)
            new_tail = new_tail.next
            mapping[old_tail] = new_tail
            old_tail = old_tail.next

        # copy randoms
        new_tail = dummy.next
        old_tail = head
        while old_tail is not None:
            if old_tail.random:
                new_tail.random = mapping[old_tail.random]
            old_tail = old_tail.next
            new_tail = new_tail.next

        return dummy.next