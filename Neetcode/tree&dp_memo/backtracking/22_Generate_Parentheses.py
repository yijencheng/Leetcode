class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = []
        def dfs(open, close):
            if len(cur) == n*2:
                ans.append("".join(cur))
                return
            if open == n:
                cur.append(")")
                dfs(open, close+1)
                cur.pop()
            elif open == close:
                cur.append("(")
                dfs(open+1, close)
                cur.pop()
            elif open>close:
                cur.append("(")
                dfs(open+1, close)
                cur.pop()
                cur.append(")")
                dfs(open, close+1)
                cur.pop()
        dfs(0,0)
        return ans
            