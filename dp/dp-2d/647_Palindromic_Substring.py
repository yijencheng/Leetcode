def countSubstrings(s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = True
            count += 1
            for j in range(i+1, len(s)):
                if j == i+1 and s[i]==s[j]:
                    dp[i][j] = True
                    count += 1
                if j>i+1 and dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j] = True
                    count += 1
        return count
