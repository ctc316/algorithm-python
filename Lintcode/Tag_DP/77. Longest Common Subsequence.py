class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        '''
            ""  A B C D
        ""  0   0 0 0 0 
        E   0   0 0 0 0 
        A   0   1 1 1 1    
        C   0   1 1 2 2
        B       1 1 2 2
        
            ""  b e d a a c b a d e
        ""  0   0 0 0 0 0 0 0 0 0 0 
        d   0   0 0 1 1 1 1 1 1 1 1
        c   0   0 0 0 1 1 2 2 2 2 2
        c
        a
        e
        e
        d
        b
        e
        b
        
        '''
        
        a_len = len(A)
        b_len = len(B)
        dp = [[0 for _ in range(a_len + 1)] for __ in range(b_len + 1)]
        for i in range(b_len):
            for j in range(a_len):
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
                if A[j] == B[i]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
                
        return dp[b_len][a_len]