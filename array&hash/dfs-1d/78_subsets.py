
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(cur, idx):
            if idx == len(nums):
                ans.append(cur)
                return
            dfs(cur, idx+1)
            dfs(cur+[nums[idx]], idx+1)
        
        dfs([], 0)
        return ans


#optimize: 
# use backtracking to record global state


#correct (but bad)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return []
        ans = []
        def dfs(trace, opts):
            ans.append(trace)            
            if len(opts) == 0:return
            
            for i, opt in enumerate(opts):
                dfs(trace+[opt], opts[i+1:])

        dfs([], nums)
        return ans


#wrong!!!!  >> [1,2], [2,1] will both be included in the answer
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return []
        ans = []
        def dfs(trace, opts):
            ans.append(trace)            
            if len(opts) == 0:return
            
            for i, opt in enumerate(opts):
                dfs(trace+[opt], opts[:i]+opts[i+1:])

        dfs([], nums)
        return ans




                