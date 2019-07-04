"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        sm_dummy = ListNode(0)
        bg_dummy = ListNode(0)
        sm_cur = sm_dummy
        bg_cur = bg_dummy
        while head:
            if head.val < x:
                sm_cur.next = head
                sm_cur = sm_cur.next
            else:
                bg_cur.next = head
                bg_cur = bg_cur.next

            temp = head.next
            head.next = None
            head = temp

        sm_cur.next = bg_dummy.next
        return sm_dummy.next