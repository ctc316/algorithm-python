class Solution:
    """
    @param n: Your money
    @param prices: Cost of each university application
    @param probability: Probability of getting the University's offer
    @return: the  highest probability
    """
    def backpackIX(self, n, prices, probability):
        dp = [0 for _ in range(n + 1)]
        price, prob, prev_prob = 0, 0, 0
        for i in range(len(prices)):
            price, prob = prices[i], probability[i]
            for j in range(n, price - 1, -1):
                prev_prob = dp[j - price]
                dp[j] = max(dp[j], prev_prob + (1 - prev_prob) * prob)

        return float(format(dp[n], '.2f'))