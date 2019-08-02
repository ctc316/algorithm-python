"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        dummy = tail = ListNode(0, head)
        while tail.next and tail.next.next:
            n1 = tail.next
            n2 = tail.next.next
            tail.next = n2
            n1.next = n2.next
            n2.next = n1
            tail = n1

        return dummy.next