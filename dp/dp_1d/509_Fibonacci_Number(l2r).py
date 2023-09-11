class Solution:
    def fib(self, n: int) -> int:
        dp = [0,1,1]
        if n<3:return dp[n]
        for i in range(3, n+1):
            dp.append(dp[i-1]+dp[i-2])

        return dp[-1]