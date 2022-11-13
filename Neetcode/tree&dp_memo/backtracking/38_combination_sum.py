# correct!
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        trace = []
        def dfs(i):
            if sum(trace) == target:
                ans.append(trace.copy())
                return
            
            for i in range(i, len(candidates)):
                add = candidates[i]
                if sum(trace)+add<=target:
                    trace.append(add)
                    dfs(i)
                    trace.pop()
        dfs(0)
        return ans




#wrong >> deplicate answer
[[2,2,3],[2,3,2],[3,2,2],[7]]

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        trace = []
        def dfs():
            if sum(trace) == target:
                ans.append(trace.copy())
                return
            
            for num in candidates:
                if sum(trace)+num<=target:
                    trace.append(num)
                    dfs()
                    trace.pop()
        dfs()        
        return ans


#wrong still! 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        trace = []
        def dfs(i):
            if sum(trace) == target:
                ans.append(trace.copy())
                return
            
            for i,num in enumerate(candidates[i:]):
                if sum(trace)+num<=target:
                    trace.append(num)
                    dfs(i)
                    trace.pop()
        dfs(0)
        return ans

#correct
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        trace = []
        def dfs(i):
            if sum(trace) == target:
                ans.append(trace.copy())
                return
            
            for start in range(i, len(candidates)):
                cur = candidates[start]
                if sum(trace)+cur<=target:
                    trace.append(cur)
                    dfs(start)
                    trace.pop()
        dfs(0)
        return ans
