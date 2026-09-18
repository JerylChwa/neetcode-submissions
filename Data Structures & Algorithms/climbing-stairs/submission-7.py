"""
at each step

f(n) = f(n-1) + f(n -2)

f(0) = 1


dp[i] = number of ways to reach lvl n from level i

dp[n] = 1
dp[n-1] = 1

populate from the back

dp[i] = dp[i+1] + dp[i+2]

dp[i] = number of ways to reach step i = dp[i-1] + dp[i-2]

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
                
        first = 1
        second = 2

        for i in range(3, n + 1):
            after = first + second
            first, second = second, after

        return second
        
        