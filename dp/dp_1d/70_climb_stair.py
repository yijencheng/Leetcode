
# l2r
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1): #  是n+1的原因是我們要求得答案是array[n]
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

# r2l
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[-1] = 1 # not zero!
        dp[-2] = 1
        for i in range(n-2,-1, -1):
            dp[i] = dp[i+1]+dp[i+2]
        return dp[0]

# improve memory
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:return 1
        a, b = 1,1
        for i in range(2,n+1):
            tmp = a+b
            a = b
            b = tmp
        return b
