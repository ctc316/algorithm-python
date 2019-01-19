class Solution:
    """
    @param cost: costs of all cards
    @param damage: damage of all cards
    @param totalMoney: total of money
    @param totalDamage: the damage you need to inflict
    @return: Determine if you can win the game
    """
    def cardGame(self, cost, damage, totalMoney, totalDamage):
        dp = [0 for _ in range(totalMoney + 1)]
        for i in range(len(cost)):
            for j in range(totalMoney, cost[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - cost[i]] + damage[i])

        return dp[totalMoney] >= totalDamage