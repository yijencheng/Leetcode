
Input: s = "abcabcbb"
Output: 3

***
when appear 2nd time
* update start to the correct place
* update appear
* update ans
 # actually no need, because the answer won't use it as last 
 # 反證：if use it at last, must have another same answer start with this value already been viewed) 

when appear 1st time
* update appear
* update ans


# correct
# 順序：判斷 check valid >> update left >> update right
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        appear = set()
        for r in range(len(s)):
            if s[r] not in appear:
                appear.add(s[r])
                longest = max(longest, r-l+1)
            else:
                while s[r] in appear:
                    appear.remove(s[l])
                    l+=1
                appear.add(s[r])

                ## no need to update longest
                    
        return longest


# cleaner: check valid + update left  >> 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appear = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in appear: # have other ways ! while s[r] not in appear: 
                appear.remove(s[l])
                l+=1
            appear.add(s[r])
            longest = max(longest, r-l+1)

        return longest



#wrong!!!
1. lenght shoudl be r-l+1
2. while should have l++
3. right should start with index=0
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appear = set()
        longest = 0
        l = 0

        for r in range(1, len(s)):
            if s[r] not in appear:
                appear.add(s[r])
                longest = max(longest, r-l)
            else:
                while s[l]!=s[r]:
                    appear.remove(s[l])
                l+=1
        return longest

# sol2: use map (have lots of needy-greedy detail...)
# wrong!!!!
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d_idx = {}
        longest = 0
        for i,ch in enumerate(s):
            if ch not in d_idx:
                d_idx[ch] = i
                longest = i+1
            else:
                longest = max(i-d_idx[ch], longest)
                d_idx[ch] = i
        return longest
                
#still wrong
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d_idx = {}
        longest = 0
        start = 0
        for i,ch in enumerate(s):
            if ch not in d_idx:
                d_idx[ch] = i
                longest = max(longest, i-start+1)
            else:
                longest = max(i-d_idx[ch], longest)
                start = d_idx[ch]+1
                d_idx[ch] = i
        return longest

#finally right!!!!!!
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d_idx = {}
        longest = 0
        start = 0
        for r,ch in enumerate(s):
            if ch not in d_idx:
                d_idx[ch] = r
                longest = max(r-start+1, longest)
            else:
                # there will be two pointer: start & previous self
                start = max(start, d_idx[ch]+1) #### important tricks
                longest = max(r-start+1, longest)
                d_idx[ch] = r
        return longest
                
                