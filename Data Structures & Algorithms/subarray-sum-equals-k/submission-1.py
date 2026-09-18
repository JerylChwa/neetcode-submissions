"""
Sum of a subarray = prefix sum of current position - prefix sum of the first position

If we calculate prefix sum -> Find every position possible sum, might as well just do it pure bruteforce

We can iterate and compute the prefixsum and just look back at all possible prefix sums computed
+ 1 if we have a prefix sum that we want


k = current_prefix - prev_prefix
prev_prefix = current_prefix - k

if prev_prefix already in hashmap, increment count by 1


[2, -1, 1, 2]

2

"""

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_seen = defaultdict(int) # We seen prefixsum of 0 once
        prev_seen[0] = 1
        prefix_sum = 0
        count = 0
        
        for num in nums:

            prefix_sum += num
            target_prefix = prefix_sum - k
            if target_prefix in prev_seen:                
                count += prev_seen[target_prefix]
            
            
            prev_seen[prefix_sum] += 1            
        
        return count


        