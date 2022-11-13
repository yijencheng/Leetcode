- P[i-1][j-1]+1, if s[i] == s[j]
- max(P[i-1][j], P[i][j-1]), if s[i] != s[j]

#wrong
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text2),len(text1) # text1 horizontal, text2 vertical
        dp = [[0]*(rows+1) for i in range(cols+1)]
        for i in range(1 ,rows+1):
            for j in range(i, cols+1):
                if text2[i] == text1[j]:dp[i][j] = dp[i-1][j-1]+1
                else: 
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[rows][cols]

#still wrong
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text2),len(text1) # text1 horizontal, text2 vertical
        dp = [[0]*(cols+1) for i in range(rows+1)]
        for i in range(1 ,rows+1):
            for j in range(i, cols+1):
                if text2[i-1] == text1[j-1]:dp[i][j] = dp[i-1][j-1]+1
                else: 
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[rows][cols]


#correct
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text2),len(text1) # text1 horizontal, text2 vertical
        dp = [[0]*(cols+1) for i in range(rows+1)]
        for i in range(1 ,rows+1):
            for j in range(1, cols+1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else: 
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[rows][cols]
                