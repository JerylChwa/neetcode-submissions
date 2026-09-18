"""
Counting sort approach
Populate freq dict of 0, 1, 2

Replace positions with 0, then 1, then 2


00 22 11

after swapping left, new element should also be relooked at

011022

"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        length = len(nums)

        i = 0
        while i <= right:                                
            if nums[i] == 0: # swap to left
                if i == left:
                    i += 1                
                else:
                    nums[i], nums[left] = nums[left], nums[i]
                    i += 1
                left += 1                
            elif nums[i] == 2: # swap to right
                if i >= right:
                    return nums
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1

        return nums

        
        
        