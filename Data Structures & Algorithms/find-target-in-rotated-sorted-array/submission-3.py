class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            
            # check if mid is in the left portion
            if nums[mid] >= nums[left]:
                if  nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # check if mid is in the right portion
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            
        