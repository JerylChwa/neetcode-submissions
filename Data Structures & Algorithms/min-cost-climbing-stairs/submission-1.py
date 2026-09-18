"""

dp[i] = minimum cost to reach ith floor

dp[i] = min(
    cost[i-1] + dp[i-1],
    cost[i-2] + dp[i-2]
)

dp[0] = 0
dp[1] = 0

dp[2] = min(
    cost[2-1] + dp[2-1],
    cost[2-2] + dp[2-2]
)

top floor = len(cost)

[1, 2, 3]
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = 0 # min cost to reach 0th floor
        second = 0 # min cost to reach 1st floor
        top_floor = len(cost)
        
        for i in range(2, top_floor + 1):
            after = min(
                cost[i-1] + second,
                cost[i-2] + first
            )

            first, second = second, after

        return second
        