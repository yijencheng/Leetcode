Input: s = "ABAB", k = 2
Output: 4


#wrong
- most importantly, the logic is totally wrong!!!!!
- pop_front should be pop_left
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(deque)
        longest = 0
        for i  in range(len(s)):
            dq = d[s[i]]
            if len(dq)<=k: # max length = k+1 
                dq.append(i)
            else:
                dq.append(i)
                dp.pop_front()
            longest = max(longest, dq[-1]-dq[0]+1)
        return longest


#correct
# Q. do we need to shrink the winodw more than 1 character?
# A. No need! 

>>> 
Given a1, b1, c1, 
if [b1, c1] is a possible solution, [a1,c1] is at least longer
hence the left should only incr by 1

another explain, see try3




class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        ans = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0)+1
            
            if (i-l+1) - max(d.values()) <=k:#valid
                ans = max(ans, i-l+1)
            else:
                d[s[l]] -=1
                l+=1 #move l after decrease the freq
        return ans

            

# ======== Optimized 
#pass, but the cur_mx is not always  correct :(
"AAABBC" >> when i=5, the cur_max =3, but should be =2
- size of window - max key's freq should always be <= k 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        cur_max = 0 # n times is the maximum of appearance
        l = 0
        ans = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0)+1
            cur_max = max(cur_max, d[s[i]])
            if (i-l+1) - cur_max <=k:#valid
                ans = max(ans, i-l+1)
            else:
                d[s[l]] -=1 
                l+=1 #move l after decrease the freq
                #no need to update cur_max >>> why? 
        return ans

#feels more correct ...
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        cur_max_key = False # n times is the maximum of appearance
        l = 0
        ans = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0)+1
            if d[s[i]] > d.get(cur_max_key, 0):
                cur_max_key = s[i]
            if (i-l+1) - d[cur_max_key] <=k:#valid
                ans = max(ans, i-l+1)
            else:
                d[s[l]] -=1 
                l+=1 #move l after decrease the freq
                #no need to update cur_max_key? >>> why?
        return ans
            
                
        
            
                
        
            
                
        