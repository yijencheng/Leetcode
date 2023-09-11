class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def dfs(cur, idx):
            if idx==len(s):
                ans.append(cur)
                return

            ch = s[idx]
            if ch.isalpha():
                upper = ch.upper()
                lower = ch.lower()
                dfs(cur+upper, idx+1)
                dfs(cur+lower, idx+1)
            else: #number
                dfs(cur+ch, idx+1)
        dfs("", 0)
        return ans
                