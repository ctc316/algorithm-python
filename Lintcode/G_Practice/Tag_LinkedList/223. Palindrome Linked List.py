"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        '''
            1->2->3->4->null       1->2   4->3
            1->2->3->4->5->null
        '''
        if head is None or head.next is None:
            return True

        mid = self.findMiddle(head)
        head2 = self.getReverseList(mid.next)
        mid.next = None

        while head2 is not None:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next

        return True


    def findMiddle(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def getReverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev