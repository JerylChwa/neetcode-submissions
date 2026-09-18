class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        

        def dfs(i, track, total):
            if total == target:
                res.append(track.copy())
                return
            if i >= len(nums) or total > target:
                return

            track.append(nums[i])
            dfs(i, track, total+nums[i])
            track.pop()
            dfs(i+1, track, total)


        


        dfs(0, [], 0)

        return res


        


