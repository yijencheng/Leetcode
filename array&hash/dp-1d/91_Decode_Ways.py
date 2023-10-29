# TBD: understand 
class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0]*len(s)
        if len(s) ==1:
            return 0 if int(s)==0 else 1
        dp[0]=0 if int(s[0])==0 else 1

        for i in range(1,len(s)):
            if i==1:
                #00-09:0             v
                #11-26:2  (10, 20: 1)
                #27-99, 個位數!=0: 1  v
                #27-99, 個位數==0 (30,40,..90): 0
                if int(s[i]) !=0:
                    dp[i]+=dp[i-1]
                if 10<=int(s[:i+1])<=26:
                    dp[i]+=1
            else:
                if int(s[i]) !=0:
                    dp[i]+=dp[i-1]
                if 10<=int(s[i-1:i+1])<=26:
                    dp[i]+=dp[i-2]

        return dp[-1]