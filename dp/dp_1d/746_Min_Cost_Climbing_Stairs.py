# l2r
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        return dp[-1]


# r2l
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(len(cost)-3,  -1, -1):
            dp[i] = cost[i]+min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])

# for dfs sol, see under dp_1d
