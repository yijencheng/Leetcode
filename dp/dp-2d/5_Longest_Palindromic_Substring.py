Ref answer: https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome
# pass
# P(i,j):
# - true: if s[i~j] is palindromic
# - false: if not
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
                    dp[i][j] = True
                elif j == i+1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res


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