class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = 0
        ret = 0
        for p in s:
            if p == '(':
                l+=1
            else:
                l-=1
                # right over-matched, provide extra left 
                if l < 0:
                   ret +=1
                   l = 0 
        return ret + l