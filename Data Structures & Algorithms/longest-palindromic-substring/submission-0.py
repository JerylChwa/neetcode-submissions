"""

dp[i][j] = (s[i] == s[j]) ^ dp[i+1][j-1]

compute i from n - 1 to 0
copute j from 0 to n - 1




"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [
            [False] * n
            for _ in range(n)
        ]

        resIdx, resLen =0, 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < j - i + 1:
                        resLen = j - i + 1
                        resIdx = i

        return s[resIdx : resIdx + resLen]
        