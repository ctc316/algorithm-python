class Solution:
    """
    @param: A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        '''
        找出res二进制表示中的某一位是1。
        对于x和y，一定是其中一个这一位是1，另一个这一位不是1
        用于记录，区分“两个”数组
        '''
        diff = 0
        for num in A:
            diff ^= num

        '''
            ...0000101    5
            ...1111011   -5
            取diff的最后一位1的位置
        '''
        diff &= -diff;


        rets = [0, 0];
        for num in A:
            # 分派給两个“不同”的数组
            if (num & diff) == 0:
                rets[0] ^= num
            else:
                rets[1] ^= num

        return rets;