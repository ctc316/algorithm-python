"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        dummy = tail = ListNode(0)
        carry = 0
        while l1 is not None or l2 is not None or carry == 1:
            tail.next = ListNode(carry)
            tail = tail.next

            if l1 is not None:
                tail.val += l1.val
                l1 = l1.next
            if l2 is not None:
                tail.val += l2.val
                l2 = l2.next

            if tail.val > 9:
                tail.val -= 10
                carry = 1
            else:
                carry = 0

        return dummy.next