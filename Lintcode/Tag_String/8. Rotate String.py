class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        '''
        abcdefg
        dcba gfe
        efgabcd

        '''
        n = len(str)
        if n == 0:
            return
        offset %= n

        self.reverseInPlace(str, 0, n - offset - 1)
        self.reverseInPlace(str, n - offset, n - 1)
        self.reverseInPlace(str, 0, n - 1)


    def reverseInPlace(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1