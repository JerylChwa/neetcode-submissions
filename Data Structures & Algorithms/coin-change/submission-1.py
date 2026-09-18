class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialise dp array
        # amount from 0 to amount, need an array of size amount + 1
        # initialise the array with maximum possible amount, amount + 1
        dp = [amount + 1]*(amount + 1)
        # dp[0] will store the min. of ways to reach amount 0
        # dp[1] will store the min. of ways to reach amount 1 etc.
        dp[0] = 0

        # iterate over every possible amount
        for money in range(1, amount + 1):
            # iterate over the diff coins
            for coin in coins:
                # check if money is big enough to be subtractable
                if money - coin >= 0:
                    # min between current no. of ways stored and 1 + min no. after subtraction
                    dp[money] = min(dp[money], dp[money-coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
        