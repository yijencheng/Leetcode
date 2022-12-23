
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


#optimize: keep global state + copy()
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        def dfs(idx):
            if idx == len(nums):
                ans.append(cur.copy())
                return
            dfs(idx+1)
            cur.append(nums[idx])
            dfs(idx+1)
            cur.pop(-1)
        
        dfs(0)
        return ans

