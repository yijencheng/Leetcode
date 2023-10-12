# greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [float('inf')]*len(nums)
        res[0] = 0
        for i in range(len(nums)):
            right = min(len(nums), i+nums[i]+1)
            for j in range(i, right):
                res[j] = min(res[j], res[i]+1)
        return res[-1]

# optimize (to be understand)
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res

