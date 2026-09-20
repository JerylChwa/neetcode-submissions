class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        is_all_neg = True
        for num in nums:
            if num > 0:
                is_all_neg = False
        
        if is_all_neg:
            return max(nums)

                


        # Find max non wrapping
        rolling_sum = 0
        max_sum = float("-inf")
        for num in nums:
            rolling_sum += num
            max_sum = max(max_sum, rolling_sum)
            if rolling_sum < 0:
                rolling_sum = 0

        
        # Find min non wrapping
        rolling_sum = 0
        min_sum = float("inf")
        for num in nums:
            rolling_sum += num
            min_sum = min(min_sum, rolling_sum)
            if rolling_sum > 0:
                rolling_sum = 0
        
        return max(max_sum, sum(nums) - min_sum)
