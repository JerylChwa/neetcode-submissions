"""
Counting sort approach
Populate freq dict of 0, 1, 2

Replace positions with 0, then 1, then 2
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0, 0, 0] # count of 0, 1, 2

        for num in nums:
            freq[num] += 1
        
        length = len(nums)
        cur_color = 0
        for i in range(length):
            while freq[cur_color] == 0:
                    cur_color += 1

            nums[i] = cur_color
            freq[cur_color] -= 1
            if freq[cur_color] == 0:
                cur_color += 1

        
        return nums
        