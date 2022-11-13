
#correct
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:return max(nums)

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            #choose i 
            opt1 = dp[i-2]+nums[i]
            #not choose i
            opt2 = dp[i-1]
            dp[i] = max(opt1, opt2)

        return dp[-1]