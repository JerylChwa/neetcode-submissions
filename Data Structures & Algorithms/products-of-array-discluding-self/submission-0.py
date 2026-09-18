class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            to_add = 1
            for j in range(len(nums)):
                
                if i != j:
                    to_add *= nums[j]

            output.append(to_add)
        return output