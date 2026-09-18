class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        output = []

        for r in range(len(nums)):
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])
            if (r-l+1) == k:
                output.append(q[0])
                if q[0] == nums[l]:
                    q.popleft()
                l+=1

        return output