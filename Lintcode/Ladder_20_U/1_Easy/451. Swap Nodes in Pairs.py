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
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next and curr.next.next:
            temp = curr.next.next
            curr.next.next = temp.next
            temp.next = curr.next
            curr.next = temp

            curr = curr.next.next

        return dummy.next