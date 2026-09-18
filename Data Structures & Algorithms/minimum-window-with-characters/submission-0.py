class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # populate the t's frequency table
        freq = defaultdict(int)
        for letter in t:
            freq[letter] += 1
        needed = len(freq)

        # sliding window that shit
        l = 0
        track = defaultdict(int)
        curr = 0
        min_l = float('inf')
        to_return = None

        for r in range(len(s)):
            track[s[r]] += 1
            if track[s[r]] == freq[s[r]]:
                curr += 1
            
            while curr == needed:
                # we found a valid window
                if (r-l+1) < min_l:
                    to_return = [l, r]
                    min_l = r-l+1
                # trim the window by popping the left element
                track[s[l]] -= 1
                if track[s[l]] < freq[s[l]]:
                    curr -= 1
                l += 1
                
        return s[to_return[0]:  to_return[1]+1] if to_return else ""