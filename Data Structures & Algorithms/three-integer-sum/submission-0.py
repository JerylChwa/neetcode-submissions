class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for i in range(len(nums)):
            # i is fixed
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -1 * nums[i]
            left = i + 1
            right = len(nums) -1
            
            

            while left < right:
                add = nums[left] + nums[right]
          
                if add < target:
                    left += 1
                elif add > target:
                    right -= 1
                elif add == target:
                   
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
 
                                           

        return output

                
            

            
                

        