class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        cur = 0
        vowels = ["a", "e", "i", "o", "u"]
        for r in range(len(s)):
            if s[r] in vowels:
                cur+=1
            if r-l+1 > k :
                if s[l] in vowels:
                    cur-=1
                l+=1
            ans = max(ans, cur)
        return ans