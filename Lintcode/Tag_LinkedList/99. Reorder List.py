"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# Version 1: Stack, Time: O(n), Space: O(n)
class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        '''
        1->2->3->4->null   1->4->2->3->null
           ^     ^
        1->2->3->4->5->null  1->5->2->4->3->null
        '''

        dummy = ListNode(0, head)
        stack = []
        tail = dummy.next
        while tail is not None:
            stack.append(tail)
            tail = tail.next

        curr = head
        while len(stack) > 0:
            tail = stack.pop()
            tail.next = None
            if tail == curr or tail == curr.next:
                return

            temp = curr.next
            curr.next = tail
            tail.next = temp
            curr = temp


# Version 2: Slow fast pointers to find middle, and split into 2 lists
class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        '''
        1->2->3->4->null   1->4->2->3->null
           ^     ^
        1->2->3->4->5->null  1->5->2->4->3->null
        '''
        if head is None or head.next is None:
            return

        # split into 2 lists
        mid = self.findMiddle(head)
        tail = self.reverse(mid.next)
        mid.next = None

        # merge
        print(head.next)
        while tail:
            next_head = head.next
            next_tail = tail.next

            head.next = tail
            tail.next = next_head

            head = next_head
            tail = next_tail


    def findMiddle(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp