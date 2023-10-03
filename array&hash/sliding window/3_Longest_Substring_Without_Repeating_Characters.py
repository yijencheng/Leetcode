# without sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            ptr = i
            sets = set()
            while ptr >= 0 and s[ptr] not in sets:
                sets.add(s[ptr])
                ptr-=1
            longest = max(longest, i-ptr)
        return longest


# correct (Best). Sliding window
class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = set()
        l=0
        for i, ch in enumerate(s):
            ## consider current, update window
            while ch in window:
                window.remove(s[l])
                l+=1
            window.add(ch)
            
            ## update ans 
            longest = max(longest, i-l+1)
        return longest


# correct, user dict to store
class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        d = {}
        l=0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0)+1
            while d[s[i]] != 1:
                d[s[l]]-=1
                l+=1
            longest = max(longest, i-l+1)
        return longest


# improve the dict soution! 
class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        d = {} # record latest appear
        l=0
        for i in range(len(s)):
            if s[i] in d:
                l = max(l, d[s[i]]+1)
            longest = max(longest, i-l+1)
            d[s[i]] = i
        return longest


# other shitty solution that works...
# correct
class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
        appear = {}
        longest = 0
        left = 0
        for i in range(len(s)):
            if appear.get(s[i],-1) <left :
                longest = max(longest, i-left+1)
            else:
                left = appear[s[i]]+1
            appear[s[i]] = i
        return longest
 
# correct
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appear = {}
        longest = 0
        left = 0
        for i in range(len(s)):
            if (s[i] not in appear) or (appear[s[i]] < left):
                longest = max(longest, i-left+1)
            else:
                left = appear[s[i]]+1
            appear[s[i]] = i
        return longest
                
