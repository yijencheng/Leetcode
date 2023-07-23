# best:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appear = set()
        left = 0
        ans = 0
        for i in range(len(s)):
            while s[i] in appear:
                appear.remove(s[left])
                left+=1
            appear.add(s[i])
            ans = max(ans, len(appear))
                
                    
        return ans