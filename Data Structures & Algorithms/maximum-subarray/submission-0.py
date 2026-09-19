class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rolling = 0
        res = float("-inf")

        for num in nums:
            rolling += num
            res = max(res, rolling)
            if rolling < 0:
                rolling = 0
            
            
        
        return res
