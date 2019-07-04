'''
Given a string s which contains only lowercase letters, 
remove duplicate letters so that every letter appear once and only once. 
You must make sure your result is the smallest in lexicographical order among 
all possible results.

Example
Example1

Input: s = "bcabc"
Output: "abc"
Example2

Input: s = "cbacdcbc"
Output: "acdb"
'''

class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def removeDuplicateLetters(self, s):
        '''
        cbacdcbc  
        a:1, b:2, c:3, d:1
        
        [c] c:2
        [b] b:1
        [a] a:0
        [a,c] c:1
        [a,c,d] d:0
        [a,c,d,b]
        '''
        
        counts = [0 for _ in range(26)]
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
            
        stack = []
        exists = set()
        for ch in s:
            if ch not in exists:
                while len(stack) > 0 and stack[-1] > ch and counts[ord(stack[-1]) - ord('a')] > 0:
                    exists.remove(stack.pop())
                stack.append(ch)
                exists.add(ch)
            counts[ord(ch) - ord('a')] -= 1 
        
        return "".join(stack)

    
