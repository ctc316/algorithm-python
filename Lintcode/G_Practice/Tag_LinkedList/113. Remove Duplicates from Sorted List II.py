"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur and cur.next:
            end = curxq
            while end.next and end.next.val == cur.val:
                end = end.next

            if cur is not end:
                prev.next = end.next
                cur = end.next
            else:
                prev = cur
                cur = cur.next

        return dummy.next