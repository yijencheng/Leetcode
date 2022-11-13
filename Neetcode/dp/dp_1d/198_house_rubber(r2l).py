class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:return max(nums)

        dp = [0]*len(nums)
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-1], nums[-2])
        for i in range(len(nums)-3, -1,-1):
            dp[i] = max(dp[i+2]+nums[i], dp[i+1])
        return dp[0]