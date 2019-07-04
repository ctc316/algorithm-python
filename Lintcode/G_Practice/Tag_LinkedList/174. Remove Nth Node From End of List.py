"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if not head or n < 0:
            return

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        i = 0
        while i < n and fast:
            fast = fast.next
            i += 1

        # if n is greater than the total number of lists
        if i != n:
            return head

        # fast is on the end of the list
        # slow is on the previous of nth node from the end of list
        while slow.next and fast.next:
            slow = slow.next
            fast = fast.next

        # disconnect the node,
        slow.next = slow.next.next

        return dummy.next