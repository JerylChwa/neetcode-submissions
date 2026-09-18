class Solution:
    def findMin(self, nums: List[int]) -> int:
  

        # 5, 1, 2, 3, 4 (mid smaller than right, store mid, search left)

        # 4, 5, 6, 7, 0, 1, 2 (mid bigger than right, store mid, search right)

        left = 0
        right = len(nums) - 1

        min_num = nums[0]

        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] < nums[right]:
                if nums[mid] < min_num:
                    min_num = nums[mid]
                right = mid - 1
            elif nums[mid] > nums[right]:
                if nums[right] < min_num:
                    min_num = nums[right]
                left = mid + 1
            else:
                if nums[mid] < min_num:
                    min_num = nums[mid]
                break
        return min_num