class Solution:
    """
    @param s: the given string
    @return: whether this string is valid
    """
    def checkValidString(self, s):
        unpaired_left = 0
        available_left = 0
        for ch in s:
            if ch == "(":
                unpaired_left += 1
                available_left += 1
            
            else: # "*" or ")"
                if unpaired_left > 0:
                    unpaired_left -= 1
                
                if ch == "*":
                    available_left += 1
                else:
                    available_left -= 1
                    if available_left < 0:
                        return False
        
        return unpaired_left == 0