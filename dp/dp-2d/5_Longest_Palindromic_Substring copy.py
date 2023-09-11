# store true/false
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        def dfs(l,r):
            if l >= r:
                return True
            if (l,r) in dp:
                return dp[(l,r)]

            if s[l] == s[r] and dfs(l+1, r-1):
                dp[(l,r)] = True
            else:
                dp[(l,r)] = False
            return dp[(l,r)]
        
        ans = s[0]
        for l in range(0, len(s)):
            for r in range(l+1, len(s)):
                if dfs(l,r) and r-l+1 > len(ans):
                    ans = s[l:r+1]
        return ans

# only store index pair, but memory exceed limit
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        def dfs(l,r):
            if l == r:
                return (l,r)
            if l > r:
                return (l,r)

            if (l,r) in dp:
                return dp[(l,r)]

            subIndx = dfs(l+1, r-1)
            if s[l] == s[r] and subIndx[1]-subIndx[0]+1 ==  (r-l+1)-2:
                    dp[(l,r)] = (l,r)
            else:
                option1=dfs(l, r-1)
                option2=dfs(l+1, r)
                if option1[1]-option1[0] > option2[1]-option2[0]:
                    dp[(l,r)] = option1
                else:
                    dp[(l,r)] = option2
            return dp[(l,r)]
        index = dfs(0, len(s)-1)
        return s[index[0]:index[1]+1]

# store entire string. memory too large 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        def dfs(l,r):
            if l == r:
                return s[l]
            if l > r:
                return ""
            if (l,r) in dp:
                return dp[(l,r)]

            if s[l] == s[r] and len(dfs(l+1, r-1)) == (r-l+1)-2:
                dp[(l,r)] = s[l]+dfs(l+1, r-1) + s[r]
            else:
                option1=dfs(l, r-1)
                option2=dfs(l+1, r)
                if len(option1) > len(option2):
                    dp[(l,r)] = option1
                else:
                    dp[(l,r)] = option2

            return dp[(l,r)]
        ans = dfs(0, len(s)-1)
        return ans