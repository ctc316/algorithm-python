"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        if not head:
            return ListNode(1)

        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        curry = 0
        nodes[-1].val += 1
        for cur in nodes[::-1]:
            cur.val += curry
            curry = 0
            if cur.val > 9:
                cur.val -= 10
                curry = 1

        if curry > 0:
            return ListNode(curry, head)

        return head