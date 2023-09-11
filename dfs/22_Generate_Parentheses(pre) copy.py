class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(cur, l,r):
            if l == n:
                ans.append(cur+(n-r)*")" )
                return
            if l == r:
                dfs(cur+"(", l+1, r)
            else:
                dfs(cur+"(", l+1, r)
                dfs(cur+")", l, r+1)
        
        dfs("", 0,0)
        return ans