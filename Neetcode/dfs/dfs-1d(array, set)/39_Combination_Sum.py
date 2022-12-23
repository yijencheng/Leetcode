class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(cur, left):
            cur_sum = sum(cur)
            if cur_sum == target:
                ans.append(cur)
                return
            for i in range(left,len(candidates)):
                if cur_sum + candidates[i] <=target:
                    dfs(cur+[candidates[i]], i)
            
        dfs([], 0)
        return ans


# try to use a global state
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        trace = []
        def dfs(i):
            if sum(trace) == target:
                ans.append(trace.copy())
                return
            
            for i in range(i, len(candidates)):
                if sum(trace)+candidates[i]<=target:
                    trace.append(add)
                    dfs(i)
                    trace.pop()
        dfs(0)
        return ans

# have repeat answer
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(cur):
            cur_sum = sum(cur)
            if cur_sum == target:
                ans.append(cur)
                return
            for c in candidates:
                if cur_sum + c <=target:
                    dfs(cur+[c])
            
        dfs([])
        return ans