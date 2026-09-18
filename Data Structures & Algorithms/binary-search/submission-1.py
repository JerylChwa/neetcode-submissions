class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) 

        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid
        
        return -1
        