class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # sort piles in order to obtain max_poss rate
        # conduct binary search on the rates from 1 to max_rate
        # start from the middle, if the rate is able to clear within h,
        # store the min_rate
        # conduct binary search on the left side
        # if the rate is unable to clear within h,
        # conduct binary search on the right side
        
        def within_time(sorted_piles : List[int], limit : int, rate : int):
            hours = 0
        
            
            for i in range(len(sorted_piles)):
                banana_hr = sorted_piles[i]
                hours += math.ceil(banana_hr/rate)
            
            return hours <= limit

        piles.sort()
        min_rate = piles[-1]

        left = 1
        right = min_rate

        

        while left <= right:
            mid = left + (right - left) // 2
            
            if within_time(piles, h, mid):
                # update min rate
                # search for smaller rate
                min_rate = mid
                right = mid - 1
            else:
                # search for bigger rate
                left = mid + 1
        return min_rate
                




        

     
        