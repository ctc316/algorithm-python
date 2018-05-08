"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# Version 1: Hash, Time: O(n), Space: O(n)
class Solution:
    """
    @param: head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        hash = set()
        node = head
        while node is not None:
            if node in hash:
                return node

            hash.add(node)
            node = node.next

        return None


# Version 2: 快慢指針, Time: O(n), Space: O(1)
class Solution:
    """
    @param: head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        if head is None or head.next is None or head.next.next is None:
            return None
            
        fast = head.next.next
        slow = head.next
        while fast != slow:
            if fast.next is None or fast.next.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
        
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow