class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        dp = [sys.maxsize for _ in range(amount + 1)]
        dp[0] = 0
        for amo in range(1, amount + 1):
            for coin in coins:
                if amo - coin >= 0:
                    dp[amo] = min(dp[amo], dp[amo - coin] + 1)

        return dp[amount] if dp[amount] != sys.maxsize else -1