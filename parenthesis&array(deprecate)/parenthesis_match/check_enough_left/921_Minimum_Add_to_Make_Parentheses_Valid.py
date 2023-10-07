class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = 0
        extra_right = 0
        for p in s:
            if p == '(':
                l+=1
            else:
                if l > 0: # right is valid and enough left
                    l-=1
                else:
                    extra_right+=1
        return l + extra_right 