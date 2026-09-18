class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        if length != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        for i in range(length):
            if s[i] != t[i]:
                return False

        return True

        
