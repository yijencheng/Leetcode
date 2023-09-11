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


# correct. Sliding window (check old first)
class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        sets = set()
        l=0
        for i in range(len(s)):
            while s[i] in sets:
                sets.remove(s[l])
                l+=1
            sets.add(s[i])
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


# use map (have lots of needy-greedy detail...)
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
                
