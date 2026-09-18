class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_l = 0
        freq = defaultdict(int)
        max_f = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_f = max(max_f, freq[s[r]])
            while (r-l+1)-max_f>k:
                freq[s[l]]-=1
                l+=1

            max_l = max(max_l, r-l+1)
        
        return max_l