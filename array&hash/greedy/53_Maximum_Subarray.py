class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        largest = nums[0]
        for num in nums:
            cur_sum = max(cur_sum+num, num)
            largest = max(largest, cur_sum)
            
        return largest