Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.




# wrong!
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = collections.Counter(t)
        d_cur = {}
        #initialize 
        for k in d.keys():
            d_cur[k] = 0

        min_window = len(s)
        l = 0
        for r, ch in enumerate(s):
            
            if ch in d.keys():
                d_cur[ch]+=1
            
            if d_cur == d: #match
                min_window = min(min_window, r-l+1)
            else:
                if d_cur[ch]>d[ch]: #too much, need to remove
                    while s[l] != ch:
                        l+=1
                    l+=1
                    d_cur = collections.Counter(s[l:r+1])
        return min_window

***
- (line 15) ch not in d.keys(), will cause KeyError
- need to find the actual string, rather than just length

- (line29) when update left pointer, it can stop on a non-key string after the while loop
- (line 24) when update d_cur, it will count non-key ch into Counter

- the logic of updating l is wrong, as the window can be >= Counter(try)
***


#still wrong. need to re-write.... 
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        d = Counter(t)
        ds = Counter(s)
        d_cur = {}
    
        #initialize 
        for ch in t:
            if ds[ch]<d[ch]:return "" #no possible answer
            d_cur[ch] = 0

        ans = s
        l = 0
        while s[l] not in t:
            l+=1
        
        for r, ch in enumerate(s):
            
            if ch in d.keys():
                d_cur[ch]+=1
            else:continue
            
            if d_cur[ch]>d[ch]: 
                while s[l] != ch:
                    if s[l] in d.keys():
                        d_cur[s[l]]-=1
                    l+=1

                d_cur[s[l]]-=1
                l+=1
                while l<len(s) and s[l] not in d:
                    l+=1
            if d_cur == d and r-l+1<len(ans): #match
                ans = s[l:r+1]
        return ans
                
                 
            