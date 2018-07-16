class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        n = len(prices)
        if n < 2:
            return 0

        # equals to unlimited transactions
        if K >= n / 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

        # mustsell[i][j]: 前i天，至多进行j次交易，第i天必须sell的最大获益，只留[i - 1][j]
        # globalbest[i][j]: 前i天，至多进行j次交易，第i天可以不sell的最大获益，只留[i - 1][j]
        mustsell = [0 for _ in range(K + 1)]
        globalbest = [0 for _ in range(K + 1)]

        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            for j in range(K, 0, -1):
                # 比較全局中少一次＋此次交易  與  前一天的交易延到今天賣
                mustsell[j] = max(globalbest[j - 1] + diff, mustsell[j] + diff)
                globalbest[j] = max(mustsell[j], globalbest[j])

        return globalbest[K]