
# 2022.11.13: there are two ways for dfs: 
# approach1. try & reject: always explore all opportunity,  and the add validity check to ensure all case are ok
# approach2. always valid: for every next step, evaluate the possibility, and only go to the valid one

This problem is `stateful`, meaning although the option is always '(' or `)`, the available `next` will be determined by current state

# try & reject
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(cur, l,r):
            if l<r:
                return
            if l == n:
                ans.append(cur+(n-r)*")" )
                return

            dfs(cur+"(", l+1, r)
            dfs(cur+")", l, r+1)
        
        dfs("", 0,0)
        return ans

# always valid
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
            
=========================
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

# sol. use cur as global param
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


            