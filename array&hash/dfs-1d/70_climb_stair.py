# TLE
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0]
        def climbStairs(cur):
            if cur == n:
                ans[0]+=1
                return
            if cur>n:
                return
                
            climbStairs(cur+1)
            climbStairs(cur+2)
        
        climbStairs(0)
        return ans[0]

# improve by cacheing