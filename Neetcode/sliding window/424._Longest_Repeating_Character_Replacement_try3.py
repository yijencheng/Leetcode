class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        longest = 0
        max_f = 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r],0)+1
            # max_f = max(max_f, d[s[r]])
            while (r-l+1) - max(d.values()) > k:
                d[s[l]]-=1
                l+=1
            longest = max(longest, r-l+1)
                
        return longest
