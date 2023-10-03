class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s = set()
        for i in range(1, len(nums)):
            cur_sum = nums[i]+nums[i-1]
            if cur_sum in s:
                return True
            s.add(cur_sum)
        return False