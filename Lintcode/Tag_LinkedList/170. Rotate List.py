"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head

        while k > 0:
            # find pos
            slow = fast = head
            rotate = 0
            while rotate < k and fast.next is not None:
                fast = fast.next
                rotate += 1

            while fast.next is not None:
                fast = fast.next
                slow = slow.next

            k -= rotate

            # move
            fast.next = head
            head = slow.next
            slow.next = None

        return head