# wrong!
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(trace,arr):
            if len(arr) <=0:return
            for i, val in enumerate(arr):
                dfs(trace.append(val), tmp.pop(i))
            ans.append(trace)

        return dfs([], nums)



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(trace,arr):
            if len(arr) <=0:
                ans.append(trace)
                return
            for i, val in enumerate(arr):
                dfs(trace+[val],arr[:i]+arr[i+1:])

        dfs([], nums)
        return ans

# set
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = set(nums)
        ans = []
        def dfs(cur, options):
            if not options:
                ans.append(cur)
                return
            for o in options:
                tmp = options.copy()
                tmp.remove(o)
                dfs(cur+[o], tmp)
        dfs([], nums)
        return ans
                
        
                