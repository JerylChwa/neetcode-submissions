"""
[3, 4, 1, -1]

[-3, 4, -1, -5]


"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            if val < 0:
                nums[i] = 0

        length = len(nums)
        
        for cur_idx, num in enumerate(nums):
            pos_num = abs(num)
            target_index = pos_num - 1
            
            if target_index >= 0 and target_index < length:
                if nums[target_index] == 0:
                    nums[target_index] = -(length+1)
                elif nums[target_index] > 0:
                    nums[target_index] *= -1
                

        # print(nums)
        for i, val in enumerate(nums):
            if val >= 0:
                return i + 1
        
        return len(nums) + 1

        