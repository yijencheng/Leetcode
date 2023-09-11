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

#correct
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






                