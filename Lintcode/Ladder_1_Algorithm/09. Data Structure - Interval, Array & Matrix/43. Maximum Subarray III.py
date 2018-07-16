class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        n = len(nums)
        if n < k:
            return 0

        '''
        典型划分类动态规划:
            localMax[k][i] 表示前i个数，取k个子数组，包含第i个数的Maximum Sum
            globalMax[k][i] 表示前i个数，取k个子数组，可以不包含第i个数的Maximum Sum

            注意初始化！！第一行不能初始化为0

            local_max表示一定要去第i个元素
            所以local_max[i - 1][j] + nums[i - 1]


                 [4,-2,-3, -1, 2, 3, 5]

                  global
            i=0   0   0    0    0    0    0    0   0
            i=1   0   4    4    4    4    4    5   10
            i=2            2    2    2    2

                  local
            i=0:  0   0    0    0    0    0    0   0
            i=1: min 4+0 -2+2 -3+0 -1+0  2+0  3+2 5+5
            i=2:     min -2+4 -3+4 -1+4  
        '''

        local_max = [[0 for _ in range(n + 1)] for __ in range(k + 1)]
        global_max = [[0 for _ in range(n + 1)] for __ in range(k + 1)]

        for i in range(1, k + 1):
            local_max[i][i - 1] = -sys.maxsize - 1
            # 小于 i 的数组不能够partition
            for j in range(i, n + 1):
                # 新的數 + max(前一個為止的local max 或 上一輪的global max)
                local_max[i][j] = nums[j - 1] + max(local_max[i][j - 1], global_max[i - 1][j - 1])
                if j == i:
                    global_max[i][j] = local_max[i][j]
                else:
                    global_max[i][j] = max(global_max[i][j - 1], local_max[i][j])


        return global_max[k][n]