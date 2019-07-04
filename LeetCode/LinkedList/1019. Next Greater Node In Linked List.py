# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        result = []
        monostack = []
        for num in reversed(nums):
            while monostack and num >= monostack[-1]:
                monostack.pop()

            result.append(monostack[-1] if monostack else 0)
            monostack.append(num)

        result.reverse()
        return result