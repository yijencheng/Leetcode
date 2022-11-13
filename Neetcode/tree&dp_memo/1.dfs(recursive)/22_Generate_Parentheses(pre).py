class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(cur, open, close):
            if len(cur) == n*2:
                ans.append(cur)
                return
            if open == n:
                dfs(cur+")", open, close+1)
            elif open == close:
                dfs(cur+"(", open+1, close)
            elif open>close:
                dfs(cur+"(", open+1, close)
                dfs(cur+")", open, close+1)
        dfs("", 0,0)
        return ans
            