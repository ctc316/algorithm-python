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
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        dummy = ListNode(0)
        while head:
            prev = self.findPos(dummy, head.val)
            new_node = ListNode(head.val, prev.next)
            prev.next = new_node
            head = head.next

        return dummy.next


    def findPos(self, dummy, val):
        prev, cur = dummy, dummy.next
        while cur and cur.val < val:
            prev = cur
            cur = cur.next

        return prev