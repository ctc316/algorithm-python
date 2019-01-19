"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            size = len(lists)
            next = []
            for i in range(0, size - 1, 2):
                next.append(self.merge(lists[i], lists[i + 1]))
            if size % 2 == 1:
                next.append(lists[-1])

            lists = next

        return lists[0]


    def merge(self, head1, head2):
        dummy = ListNode(0)
        curr = dummy
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                curr = head1
                head1 = head1.next
            else:
                curr.next = head2
                curr = head2
                head2 = head2.next

        if head1 is not None:
            curr.next = head1

        if head2 is not None:
            curr.next = head2

        return dummy.next