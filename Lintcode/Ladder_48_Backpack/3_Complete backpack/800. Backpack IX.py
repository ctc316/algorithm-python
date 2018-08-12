class Solution:
    """
    @param n: Your money
    @param prices: Cost of each university application
    @param probability: Probability of getting the University's offer
    @return: the  highest probability
    """
    def backpackIX(self, n, prices, probability):
        dp = [0 for _ in range(n + 1)]
        for i in range(len(prices)):
            for j in range(n, prices[i] - 1, -1):
                prev_prob = dp[j - prices[i]]
                dp[j] = max(dp[j], prev_prob + (1 - prev_prob) * probability[i])

        return float(dp[n])