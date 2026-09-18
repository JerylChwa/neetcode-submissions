class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointer approach, if less than target move right pointer, if more than
        # target, move left pointer

        left = 0
        right = len(numbers) - 1

        while numbers[left] < numbers[right]:
            add = numbers[left] + numbers[right]
            if add < target:
                left += 1
            elif add > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        
        return [left + 1, right + 1]

        