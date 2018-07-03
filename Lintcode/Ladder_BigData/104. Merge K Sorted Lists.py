"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# Version 1: Sorting
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        results = []
        for node in lists:
            while node:
                results.append(node.val)
                node = node.next

        results.sort()

        dummy = ListNode(0)
        tail = dummy
        for ele in results:
            tail.next = ListNode(ele)
            tail = tail.next

        return dummy.next