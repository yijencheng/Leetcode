class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        l = 0
        def isPalindrome(l, r):
            while l < r and s[l] == s[r]:
                l+=1
                r-=1
            return l>=r

        for r in range(len(s)):
            ch = s[r]
            # find the max palindrome ending with s[r]
            l = max(l-1, 0)
            while l <r  and not isPalindrome(l,r):
                l+=1

            if r-l+1 > len(ans):
                ans = s[l:r+1]
        return ans
