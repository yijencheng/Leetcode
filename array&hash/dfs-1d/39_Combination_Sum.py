# important: The same number may be chosen from candidates an unlimited number of times
Solution 1: with for-loop
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


# wrong: have repeat answer
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

Sol2: without for loop
# wrong: cannot select repeat element
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(cur, i):
            cur_sum = sum(cur)
            if cur_sum == target:
                ans.append(cur)
                return
            elif cur_sum > target:
                return

            if i == len(candidates):return
            
            
            dfs(cur, i+1)
            dfs(cur+[candidates[i]], i+1)
            
        dfs([], 0)
        return ans

# fix! 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(cur, i):
            cur_sum = sum(cur)
            if cur_sum == target:
                ans.append(cur)
                return
            elif cur_sum > target:
                return

            if i == len(candidates):return
            
            dfs(cur+[candidates[i]], i)
            dfs(cur, i+1)
            
        dfs([], 0)
        return ans