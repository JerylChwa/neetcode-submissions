"""
Finding max subarray sum
- Iterate from L to R
- Compute max possible subarray ending at current element
- We either extend the previous subarray, or start a new subarray

Finding min subarray sum
- Iterate from L to R
- Compute min possible subarray ending at current element
- We either extend the previous subarray, or start a new subarray
"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = 0
        cur_min = float("inf")
        global_max = 0
        global_min = float("inf")
        total = 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)
            global_max = max(global_max, cur_max)
            global_min = min(global_min, cur_min)
            total += num
        
        return max(global_max, total - global_min) if global_max > 0 else max(nums)
