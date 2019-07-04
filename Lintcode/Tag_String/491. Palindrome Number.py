class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        num = str(num)
        return num == num[::-1]




class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        if num < 0 :
            return False
        tmp = num
        rev = 0
        while tmp :
            rev = rev * 10 + tmp % 10
            tmp //= 10
        return rev == num