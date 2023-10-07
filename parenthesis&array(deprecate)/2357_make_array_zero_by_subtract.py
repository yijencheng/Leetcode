class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in s:
            if num != 0:
                ans+=1
        return ans