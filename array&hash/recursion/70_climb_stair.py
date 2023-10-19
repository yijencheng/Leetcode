# 遞迴式. 2^n
# 跟55. jump game有點像



# 遞迴式. TLE
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:return 1
        return self.climbStairs(n-2)+self.climbStairs(n-1)

# improve by cacheing (x)