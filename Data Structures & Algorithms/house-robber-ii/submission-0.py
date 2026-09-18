"""
States : 
-Robbed first 
-Current index

dfs(0, False) -> max(nums[0]+dfs(2, True), dfs(1, False))

dfs(2, True) -> max(nums[4]+dfs(4, True), dfs(3, True))

dfs(1, False) -> max(nums[1] + dfs(3, False), dfs(2, False))

dfs(n-1, False) -> max(nums[n-1] + dfs(n), dfs(n+1, False))

dfs(n-1, True) -> return 0
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        mem = [
            [-1 for _ in range(length+2)]
            for _ in range(2)
        ] # mem[0][0] : value of (i=0, first=False)
        
        def dfs(i, first):
            second_index = 1 if first else 0
            if mem[second_index][i] != -1:
                return mem[second_index][i]
            
            if i >= length or (i == length -1 and first == True):
                mem[second_index][i] = 0
                return mem[second_index][i]
            
            if i == 0:
                mem[second_index][i] = max(
                    nums[0] + dfs(i+2, True),
                    dfs(i+1, False)
                )
                return mem[i][second_index]
            mem[second_index][i] = max(
                nums[i] + dfs(i+2, first),
                dfs(i+1, first)
            )
            return mem[second_index][i]


        return dfs(0, False)
        



        
        