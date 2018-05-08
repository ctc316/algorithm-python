class Pair:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val
    
    def __lt__(self, other):
         return self.val < other.val

        
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if len(numbers) < 2:
            return [-1, -1]
        
        pairs = []
        for i in range(len(numbers)):
            pairs.append(Pair(i, numbers[i]))
        
        pairs.sort()
        
        left = 0
        right = len(pairs) - 1
        while left < right:
            remain = target - pairs[left].val - pairs[right].val
            if remain == 0:
                idx1 = pairs[left].idx
                idx2 = pairs[right].idx
                
                if idx1 > idx2:
                    return [idx2, idx1]
                return [idx1, idx2]
                
            elif remain < 0:
                right -= 1
            
            else:
                left += 1
        
        return [-1, -1]