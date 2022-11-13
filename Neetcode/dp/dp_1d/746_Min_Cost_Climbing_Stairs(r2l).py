Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.



從i~dst = (i+1~dst) + (i+2~dst)


#correct
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(len(cost)-3,  -1, -1):
            dp[i] = cost[i]+min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])

# wrong!!!!!!
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(len(cost)-3,  -1, -1):
            dp[i] = cost[i]+min(cost[i+1], cost[i+2]) # >>> 是看dp[i+1] & dp[i+2]
        
        return min(dp[0], dp[1])