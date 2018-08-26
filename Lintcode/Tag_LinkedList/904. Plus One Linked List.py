"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        if head is None:
            return head

        tail = head
        stack = []
        while tail.next != None:
            stack.append(tail)
            tail = tail.next

        tail.val += 1

        while tail.val > 9 and len(stack) > 0:
            tail.val %= 10
            tail = stack.pop()
            tail.val += 1

        if head.val > 9:
            head.val %= 10
            head = ListNode(1, head)

        return head