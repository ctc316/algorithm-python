class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def subSum(self, n):

        '''
        1, 2, 3

        1   12   13 123  14 124 134 1234

        1    1      2       4
        '''
        # if n == 1:
        #     return n

        summ = 0
        combins = 1
        for i in range(1, n + 1):
            summ += i
            combins *= 2

        return summ * combins//2