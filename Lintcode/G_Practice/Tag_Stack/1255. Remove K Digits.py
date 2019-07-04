'''
Given a non-negative integer num represented as a string, remove k digits
from the number so that the new number is the smallest possible.

The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
'''



class Solution:
    """
    @param num: a string
    @param k: an integer
    @return: return a string
    """
    def removeKdigits(self, num, k):
        '''
        101121246

        res: 1,    k: 2
        res: 11    k: 1
        res: 111   k: 1
        res: 1111  k: 0
        res: 1111246
        '''
        if not num or k == 0:
            return num

        res = []
        for i in range(len(num)):
            while len(res) > 0 and k > 0 and res[-1] > num[i]:
                res.pop()
                k -= 1
            if num[i] != '0' or len(res) > 0 :
                res.append(num[i])

        while len(res) > 0 and k > 0:
            res.pop()
            k -= 1

        return ''.join(res) if len(res) != 0 else '0'