Input: s = "ABAB", k = 2
Output: 4


#correct!
# add first 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        longest = 0
        max_f = 0 #important!
        for r in range(len(s)):
            d[s[r]] = d.get(s[r],0)+1
            max_f = max(max_f, d[s[r]])
            while (r-l+1) - max_f > k: #this new element make it explode! hence need to update left
                d[s[l]]-=1
                max_f = max(max_f, d[s[l]])
                l+=1
            longest = max(longest, r-l+1)
                
        return longest


# also correct 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        longest = 0
        max_f = 0 #important!
        for r in range(len(s)):
            d[s[r]] = d.get(s[r],0)+1
            max_f = max(max_f, d[s[r]])
            if (r-l+1) - max_f > k: # this is also valid, cool isn't it? see explain in try2
                d[s[l]]-=1
                l+=1
            else:
                longest = max(longest, r-l+1)
                
        return longest


#wrong..
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        longest = 0
        max_f = 0 #important!
        for r in range(len(s)):
            d[s[r]] = d.get(s[r],0)+1
            max_f = max(max_f, d[s[r]])
            if (r-l+1) - max_f > k: #this right make it explode!
                d[s[r]]-=1
                max_f = max(max_f, d[s[r]])
            else:
                longest = max(longest, r-l+1)
                
        return longest
            

            
                
        
            
                
        