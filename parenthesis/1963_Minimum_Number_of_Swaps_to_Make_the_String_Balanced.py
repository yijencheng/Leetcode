
#suggested 
#intuition (pass)
class Solution:
    def minSwaps(self, s: str) -> int:
        l, r = 0, len(s)-1
        s_l, s_r = 0,0 
        swap = 0
        while l<r:
            while l<len(s) and s_l>=0: # important to add out-of-bound check
                if s[l] == '[':
                    s_l+=1
                else:
                    s_l-=1
                l+=1
                
            while r >=0 and s_r>=0: # important to add out-of-bound check
                if s[r] == ']':
                    s_r+=1
                else:
                    s_r-=1
                r-=1
            
            if l>=len(s) or r <0:break #important
            swap+=1
            s_l,s_r = s_l+2,s_r+2 
        return swap
            
