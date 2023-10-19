# TLE recursion
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def canJumpI(i):
            if i == len(nums)-1:
                return True
            for step in range(1,nums[i]+1):
                if canJumpI(i+step):
                    return True
        return canJumpI(0)

# improve by cacheing