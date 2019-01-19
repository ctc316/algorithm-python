class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isValid(s[left: right]) or self.isValid(s[left + 1: right + 1])
            
            left += 1
            right -= 1
        
        return True
                
                
    def isValid(self, s):
        left = 0 
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True