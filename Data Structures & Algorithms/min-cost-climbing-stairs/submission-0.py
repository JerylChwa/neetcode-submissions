class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # cost is  [1, 2, 3, 0]
        # each index shall represent the lowest cost to reach last index from
        # that paticular index
        # @ last index, cost to reach last index is 0
        # @ second last index, cost to reach last index is cost of curr index
        # since its just taking 1 step
        # @ third last index, cost to reach last index is curr index cost
        # + the minimum of cost to reach from curr+1 index and curr+2 idnex
        # start from third last index

        cost.append(0)

        for i in range(len(cost) -3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])




        
        