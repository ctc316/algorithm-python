class Solution:
    """
    @param: A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        '''
        找出二進制表示中的某一位是1。
        對於x和y，必定其中一個數的這一位是1，另一個數的這一位不是1
        因此可以先找出這一位，用來區分“两個”数组
        '''
        diff = 0
        for num in A:
            diff ^= num

        '''
            ...0000101    5
            ...1111011   -5
            取diff的最後一位1的位置
        '''
        diff &= -diff;


        results = [0, 0];
        for num in A:
            # 分派給两個“不同”的數組
            if (num & diff) == 0:
                results[0] ^= num
            else:
                results[1] ^= num

        return results;