class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashy:
                return [hashy[complement], i]
            else:
                hashy[nums[i]] = i
