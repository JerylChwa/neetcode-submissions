class Solution:
    def maxArea(self, height: List[int]) -> int:
        highest_vol = 0
        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] >= height[right]:
                vol = (right - left)*height[right]
                #print("left is " + str(left) + " right is " + str(right) + " vol : " + str(vol))
                right -= 1
            else:
                vol = (right - left)*height[left]
                #print("left is " + str(left) + " right is " + str(right) + "vol : " + str(vol))
                left += 1

            if vol > highest_vol:
                highest_vol = vol
            
        return highest_vol