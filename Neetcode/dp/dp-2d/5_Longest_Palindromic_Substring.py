Ref answer: https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome


# improve space, pass
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        if len(set(s)) == 1:return s ## handle special case

        res = ""
        dp = [None for i in range(len(s))]        
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[i] = True
                elif j == i+1:
                    dp[i] = (s[i] == s[j])
                else:
                    dp[i] = (dp[i+1] and s[i] == s[j])
                if dp[i] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res

# pass
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        if len(set(s)) == 1:return s ## handle special case

        res = ""
        dp = [[None for i in range(len(s))] for j in range(len(s))]        
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[j][i] = True
                elif j == i+1:
                    dp[j][i] = (s[i] == s[j])
                else:
                    dp[j][i] = (dp[j-1][i+1] and s[i] == s[j])
                if dp[j][i] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res