class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        '''
        n           = 1000
        n - 1       = 0111
        n & (n - 1) = 0000
        '''
        
        return n > 0 and (n & (n - 1)) == 0