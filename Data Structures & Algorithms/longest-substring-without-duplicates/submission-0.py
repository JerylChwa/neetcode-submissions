class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        highest = 0
        l = 0

        for i in range(len(s)):
            while s[i] in track:
                track.remove(s[l])
                l+=1
            
            track.add(s[i])
            highest = max(highest, i-l+1)

        return highest
        