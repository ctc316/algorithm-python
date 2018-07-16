"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

# Version 1: Brute Force, Time: O(n^2), Space: O(1)
class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        while p1 is not None:
            p2 = headB
            while p2 is not None:
                if p1 is p2:
                    return p1
                p2 = p2.next

            p1 = p1.next

        return None


# Version 2: HashSet, Time: O(n), Space: O(n)
class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):

        p1 = headA
        p1Set = set()
        while p1 is not None:
            p1Set.add(p1)
            p1 = p1.next

        p2 = headB
        while p2 is not None:
            if p2 in p1Set:
                return p2
            p2 = p2.next

        return None



# Version 3: Remove extra nodes, Time: O(n), Space: O(1)
class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # count nodes in list A, B
        lenA, lenB = 0, 0
        p1, p2 = headA, headB
        while p1 is not None:
            lenA += 1
            p1 = p1.next
        while p2 is not None:
            lenB += 1
            p2 = p2.next
        
        # ignore nodes of extra len
        p1, p2 = headA, headB
        while lenA > lenB:
            p1 = p1.next
            lenA -= 1
        while lenB > lenA:
            p2 = p2.next
            lenB -= 1
        
        # find intersection node    
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1


# Version 4: Find Cycle, Time: O(n), Space: O(1)
class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        
        # get tail of list A and link it to list B
        tailA = headA
        while tailA.next is not None:
            tailA = tailA.next
        tailA.next = headB
        
        # find the cycle in list A
        node = self.findCycleInList(headA)
        
        # recover list A
        tailA.next = None
        
        return node
        
    def findCycleInList(self, head):
        slow = head
        fast = head.next
        
        '''
                        --------------------------
                       |                          |
           a1 → a2 -> c1 -> c2 -> c3 -> b1 → b2 → b3
           s    f
                s            f    
                      s                 f
                             s                    f
                             f     s
                                        sf
                                   
        '''
        
        # check for cycle existence
        while slow is not fast:
            if fast is None or fast.next is None:
                return None
            
            slow = slow.next
            fast = fast.next.next
        
        
        # get the cycle start point
        slow = head
        fast = fast.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        
        return slow



