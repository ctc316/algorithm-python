class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        ones = 0;
        twos = 0;

        '''
        对 ones操作， ones = ones ^ A[i] & (~tows)
        把A[i] 计入到出现一次的情况里，但有可能这个数已经出现过两次，所以要排除两次情况

        对 twos操作， twos = twos ^ A[i] & (~ones) 把A[i]
        计入到两次情况，
            如果第三次出现了，自然消掉了，
            如果第二次出现，那么就计入，
            如果是第一次出现，不计入，这个过程通过和ones的非相交来控制
        '''

        for i in range(len(A)):
            ones = (ones ^ A[i]) & (~ twos)
            twos = (twos ^ A[i]) & (~ ones)

        return ones;