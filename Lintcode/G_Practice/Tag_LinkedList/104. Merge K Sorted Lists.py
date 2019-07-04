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
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            n = len(lists)
            for i in range(1, n, 2):
                lists.append(self.merge2Lists(lists[i - 1], lists[i]))
            lists = lists[n - (n % 2):]

        return lists[0]


    def merge2Lists(self, head1, head2):
        dummy = ListNode(0)
        cur = dummy
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head1:
            cur.next = head1
        elif head2:
            cur.next = head2

        return dummy.next




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
        pts = {i:v for i, v in enumerate(lists)}
        dummy = ListNode(0)
        cur = dummy
        while len(pts) > 0:
            min_idx = []
            minimum = float("Inf")
            nones = []
            for i, pt in pts.items():
                if not pt:
                    nones.append(i)
                    continue

                if pt.val == minimum:
                    min_idx.append(i)

                if pt.val < minimum:
                    min_idx = [i]
                    minimum = pt.val

            for i in nones:
                del pts[i]

            if not min_idx:
                continue

            for i in min_idx:
                temp = pts[i]
                pts[i] = pts[i].next
                temp.next = None
                cur.next = temp
                cur = cur.next

        return dummy.next