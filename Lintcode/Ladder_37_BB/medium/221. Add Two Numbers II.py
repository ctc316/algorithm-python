"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        r1 = self.getReversedList(l1)
        r2 = self.getReversedList(l2)
        carry = 0
        dummy = tail = ListNode(0)
        while r1 or r2 or carry:
            if r1:
                carry += r1.val
                r1 = r1.next
            if r2:
                carry += r2.val
                r2 = r2.next

            tail.next = ListNode(carry % 10)
            tail = tail.next
            carry //= 10

        return self.getReversedList(dummy.next)


    def getReversedList(self, head):
        dummy = ListNode(0)
        while head:
            dummy.next = ListNode(head.val, dummy.next)
            head = head.next

        return dummy.next