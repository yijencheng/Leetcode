    # ---abcde(text1)---
    # -
    # a
    # c
    # e

    # if x[0] == y[0]: ans = 1+longestCommonSubsequence(x[1:], y[1:])
    # if x[0] != y[0]: ans = max(longestCommonSubsequence(x[1:], y), longestCommonSubsequence(x, y[1:]))


# what does dp[i][j] means? 

# >>> 代表 text2[i:], text1[j:] 
# ex. text1=abcde, text2=ace, i,j=2,2  >>> dp[1][2] = ce & cde 的 LCS （由後往前）


- P[i-1][j-1]+1, if s[i] == s[j]
- max(P[i-1][j], P[i][j-1]), if s[i] != s[j]


#wrong!!!
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text1),len(text2)
        
        ans = 0
        dp = [[0]*(rows+1) for i in range(cols+1)]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1, -1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
                ans = max(ans, dp[i][j])
        return ans



# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  

#some redundancy
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text2),len(text1)
        
        ans = 0
        dp = [[0]*(cols+1) for i in range(rows+1)]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1, -1,-1):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
                ans = max(ans, dp[i][j])
        return ans

#correct
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text2),len(text1)
        dp = [[0]*(cols+1) for i in range(rows+1)]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1, -1,-1):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
        return dp[0][0]
                