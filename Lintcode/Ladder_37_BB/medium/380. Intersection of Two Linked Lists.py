"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        '''
        1 2 3
              4 5
          9 8
                     ===
        1 2 3 4 5 9 8 4 5
        9 8 4 5 1 2 3 4 5
                     ===
        two nodes will eventually be the same
        '''
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a