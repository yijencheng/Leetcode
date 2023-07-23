class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        max_length = 0
        cur_sum = 0
        l=0
        for r in range(len(nums)):
            cur_sum+=nums[r]
            while nums[r]*(r-l+1) - cur_sum >k:
                cur_sum-=nums[l]
                l+=1
            max_length = max(max_length, r-l+1)
        return max_length 