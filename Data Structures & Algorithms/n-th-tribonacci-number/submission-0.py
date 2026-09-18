class Solution:
    def tribonacci(self, n: int) -> int:

        first = 0
        second = 1
        third = 1
        if n <= 0:
            return 0        
        if n <= 2:
            return 1

        for _ in range(n-2):
            after = first + second + third
            first, second, third = second, third, after
        
        return third
        