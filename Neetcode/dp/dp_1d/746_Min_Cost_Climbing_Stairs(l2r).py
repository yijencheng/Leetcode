from urllib.parse import non_hierarchical
import xdrlib

[10, 15, 20] dst
走到最後一格 (dst)的cost = 走到array[-2] + 走到array[-1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
    
        return dp[-1]