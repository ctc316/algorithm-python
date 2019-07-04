"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        '''
        1->2->3->4->5    2, 4     need n - 1, m + 1
           i        j
         <-2<-3<-4<-5    4-2 + 1
        '''
        if m < 1:
            m = 1
        if n < m:
            return head

        dummy = ListNode(0, head)
        node_prev_m = self.findNthNode(dummy, m - 1)
        node_m = node_prev_m.next
        node_n = self.findNthNode(dummy, n)
        node_post_n = node_n.next
        
        self.reverseNNodes(node_m, n - m)
        node_prev_m.next = node_n
        node_m.next = node_post_n

        return dummy.next


    def reverseNNodes(self, start, n):
        i = 0
        prev = start
        cur = start.next
        while i < n and prev and cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            i += 1


    def findNthNode(self, dummyhead, n):
        i = 0
        node = dummyhead
        while node and i < n:
            node = node.next
            i += 1

        return node