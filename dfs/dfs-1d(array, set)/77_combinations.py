class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(cur, l, r):
            if len(cur) == k:
                ans.append(cur)
                return
            for i in range(l,r+1):
                dfs(cur+[i+1], i+1, r+1)
        dfs([], 0, n-k)
        return ans