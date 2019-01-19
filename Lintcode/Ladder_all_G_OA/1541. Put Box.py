class Solution:
    """
    @param box: the boxes
    @param position: the positions
    @return:  the maximum number of boxes you can put in
    """
    def putBox(self, box, position):
        '''
            0  1 2 3 4
         0  0  0 0 0 0
         4  0  0 0 0 1
         2  0  0 1 1 1
         3  0  0 1 2 2
         1  0  1 1 2 3
        '''

        n_box = len(box)
        n_pos = len(position)
        dp = [[0 for _ in range(n_pos + 1)] for __ in range(n_box + 1)]
        for i in range(n_box):
            for j in range(n_pos):
                if box[i] <= position[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[n_box][n_pos]