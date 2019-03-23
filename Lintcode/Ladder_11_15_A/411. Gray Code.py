class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        '''
              0
              1

             11
             10

            110
            111
            101
            100

           1100
           1101
           1111
           1110
           1010
           1011
           1001
           1000

        '''
        ans = [0]
        for bit in range(0, n):
            for i in range(len(ans) - 1, -1, -1):
                ans.append(pow(2, bit) + ans[i])

        return ans



# Version 2: Gray Code Formula: G(i) = i ^ (i / 2)
class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        '''
              0       0 ^ 0
              1       1 ^ 0
            
             11       2 ^ 1  (10 ^ 01 = 11)
             10       3 ^ 1  (11 ^ 01 = 10)
            
            110
            111
            101
            100
        '''
        ans = []
        for i in range(0, 1 << n):
            ans.append(i ^ (i >> 1))
                
        return ans