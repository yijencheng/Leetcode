# will be equivalent to dp r2l 
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(nums):
               return 0
            if i in dp:
                return dp[i]
            dp[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return dp[i]
        return dfs(0)
