"""
all upper case letters
k : replacements of any letters with any other uppercase english letters

"""
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        longest = 0
        most_freq = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            most_freq = max(most_freq, freq[s[r]])
            length = r - l + 1
            changes_needed = length - most_freq

            while r - l + 1 - most_freq > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            
            longest = max(longest, r - l + 1)

        return longest
                
            





        