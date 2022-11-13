from contextlib import nullcontext


P(i,j):
- true, if P(i+1, j-1) and s[i] == s[j]
- false, otherwise


#wrong!  >
# >>
# >> 填寫的順序錯誤了，導致0其實是還沒填，誤判為不等於
"babad" >> null

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*len(s) for i in range(len(s))]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==j:
                    dp[i][j]=1
                elif j-i==1:
                    dp[i][j]=1 if dp[i][j] == dp[i][j-1] else 0
                else:
                    if s[i]== s[j] and dp[i+1][j-1] == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*len(s) for i in range(len(s))]
        ans = ""
        
        #p5
        for i in range(len(dp)-1,-1,-1):
            for j in range(i, len(dp[0])):
                if i==j:
                    dp[i][j]=1
                elif s[i] == s[j]:
                    if j-i==1 or dp[i+1][j-1] == 1:
                        dp[i][j]=1
                
                if dp[i][j] == 1 and j-i+1>len(ans):
                    ans = s[i:j+1]
        return ans
    