"""
dp[i] = maximum amount we can steal from house i onwards

dp[len(nums)] = 0
dp[len(nums) - 1] = nums[len(nums) - 1]

dp[i] = max(nums[i] + dp[i+2], dp[i+1])

return dp[0]
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        

        right = 0
        left= nums[len(nums)-1]

        for i in range(length-2, -1, -1):
            after = max(
                nums[i] + right,
                left
            )

            left, right = after, left
        
        return left
        