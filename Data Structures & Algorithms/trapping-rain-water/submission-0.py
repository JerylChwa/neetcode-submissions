class Solution:
    def trap(self, height: List[int]) -> int:
        left  = 0
        right = len(height) - 1

        max_l = height[left]
        max_r = height[right]

        to_add = 0

        while left < right:
            if height[left] <= height[right]: # left shorter than right -> add based on left height
                # check if its lower than max height -> if lower, can add water
                if height[left] < max_l:
                    to_add += max_l - height[left]
                    left += 1
                else:
                    max_l = height[left]
                    left += 1
            else: # height[left] > height[right] : -> add based on right height
                if height[right] < max_r:
                    to_add += max_r - height[right]
                    right -= 1
                else:
                    max_r = height[right]
                    right -= 1
        
        return to_add

