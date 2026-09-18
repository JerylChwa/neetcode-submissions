class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, track, total):
            if total == target:
                res.append(track.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            track.append(candidates[i])
            dfs(i+1, track, total+candidates[i])
            track.pop()
            while i+1<len(candidates) and candidates[i+1] == candidates[i]:
                i+=1
            dfs(i+1, track, total)


        dfs(0, [], 0)
        return res
        