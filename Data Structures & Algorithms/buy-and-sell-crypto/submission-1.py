class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_smallest = float("inf")
        profit = 0
        for p in prices:
            profit = max(profit, p - prev_smallest)
            prev_smallest = min(prev_smallest, p)

        return profit

    
            

        
