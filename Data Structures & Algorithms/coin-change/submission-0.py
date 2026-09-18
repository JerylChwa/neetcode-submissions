class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # dp[0] : fewest no. of coins needed to make 0
        # do[1] : fewest no. of coins needed to make 1
        for money in range(1, amount + 1):
            for coin in coins:
                if money - coin >= 0:
                    dp[money] = min(dp[money], 1 + dp[money-coin])
        
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1

        