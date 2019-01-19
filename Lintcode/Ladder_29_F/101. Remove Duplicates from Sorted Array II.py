class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, num):
        n = len(num)
        if n < 3:
            return n
    
        i = 1
        j = 2
        while j < n:
            while j < n and num[j] == num[i] and num[j] == num[i - 1]:
                j += 1
    
            if j >= n:
                break
    
            i += 1
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
    
            j += 1
    
        return i + 1