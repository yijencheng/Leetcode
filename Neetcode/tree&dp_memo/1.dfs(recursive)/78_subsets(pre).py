class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return [[]]
        ans = []
        def dfs(cur, idx):
            if idx == len(nums):
                ans.append(cur)
                return
            dfs(cur, idx+1)
            dfs(cur+[nums[idx]], idx+1)
        
        dfs([], 0)
        return ans
