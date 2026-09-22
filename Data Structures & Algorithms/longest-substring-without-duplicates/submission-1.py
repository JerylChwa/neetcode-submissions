"""
Invariant within sliding window : No duplicate characters

2 pointers
if new element exists in the set, we need to keep removing elements from the left pointer onwards
until the new element is no longer in the set

then exit the while loop and add it to the set

then contunue shifting the right pointer

at the same time just keep track of the maximum window
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        max_window = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            max_window = max(max_window, r - l + 1)
        
        return max_window


        