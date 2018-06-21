# Version 1: Data Stream 處理

# class ListNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
        
class DataStream:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head
        self.numToPrev = {}
        self.duplicates = set()
        
    def remove(self, number):
        prev = self.numToPrev[number]
        prev.next = prev.next.next
        
        if prev.next:
            self.numToPrev[prev.next.val] = prev
        else:
            self.tail = prev
    
    def add(self, number):
        if number in self.duplicates:
            return
        
        if number in self.numToPrev:
            self.remove(number)
            self.duplicates.add(number)
        else:
            self.tail.next = ListNode(number)
            self.numToPrev[number] = self.tail
            self.tail = self.tail.next
            
    def firstUnique(self):
        if self.head.next:
            return self.head.next.val
        
        return -1
        
        
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        ds = DataStream()
        for n in nums:
            ds.add(n)
            if n == number:
                return ds.firstUnique()
        
        return -1



# Version 2: 不考慮 Data Stream

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        n = len(nums)
        firstNumPos = {}
        uniques = [False for i in range(n)]

        for i in range(n):
            if nums[i] in firstNumPos:
                uniques[firstNumPos[nums[i]]] = False
            else:
                uniques[i] = True
                firstNumPos[nums[i]] = i

            if nums[i] == number:
                for j in range(n):
                    if uniques[j]:
                        return nums[j]

        return -1