class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        '''
        因为只有一个数恰好出现一个，剩下的都出现过两次，所以只要将所有的数异或起来，
        就可以得到唯一的那个数，因为相同的数出现的两次，异或两次等价于没有任何操作！
        '''

        num = 0
        for n in A:
            num ^= n

        return num