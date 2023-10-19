
# l2r. 
# dp[i]=k stands for there are "k" possbile ways to travel from 0~i
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1): #  是n+1的原因是我們要求的答案是dp[n]
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

# improve memory
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:return 1
        a, b = 1,1
        for i in range(2,n+1):
            
            # a, b = b, a+b
            tmp = a+b
            a = b
            b = tmp
        return b

# r2l
# dp[i]=k stands for there are "k" possbile ways to travel from i to n
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[-1] = 1 # not zero!
        dp[-2] = 1
        for i in range(n-2,-1, -1):
            dp[i] = dp[i+1]+dp[i+2]
        return dp[0]















