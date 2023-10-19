# l2r
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1:return max(nums) # if length less than 2 

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  # dp[i] = maximum rob from 0~i
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

# equivalent to l2r
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1:return max(nums)

        dp ={}
        # [0,i] = max([0,i-2]+nums[i], [0,i-1])
        def dfs(i):
            if i < 0:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(dfs(i-2)+nums[i], dfs(i-1)) 
            return dp[i]
        return dfs(len(nums)-1)


# r2l
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:return max(nums)

        dp = [0]*len(nums)
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-1], nums[-2])
        for i in range(len(nums)-3, -1,-1):
            dp[i] = max(dp[i+2]+nums[i], dp[i+1])
        return dp[0]
    