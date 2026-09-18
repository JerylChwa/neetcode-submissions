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
        count = [0] * 3

        for num in nums:
            count[num] += 1
        
        index = 0
        for i in range(3):
            while count[i]:
                nums[index] = i
                index += 1
                count[i] -= 1
        
        return nums

        
        
        