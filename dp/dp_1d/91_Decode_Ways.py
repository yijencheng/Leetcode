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


# solve! but ugly
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i-2] + dp[i-1], if s[-2:] >=10 <=26
        # dp[i-1], otherwise
        if s[0] == '0':return 0

        if len(s)<=1:return 1
        def canBreak(s):
            return 0<int(s[0]) and int(s[0]) <=9 and 0<int(s[1]) and int(s[1]) <=9 and int(s) <= 26 

        dp = [0]*len(s)
        dp[0] = 1
        if canBreak(s[0:2]):
            dp[1] = 2
        else:
            if s[0:2] == "10" or s[0:2] == "20":
                dp[1] = 1
            elif s[1] == '0':
                return 0
            else: # >26 or <10 
                dp[1] = 1

        for i in range(2, len(s)):
            prev2 = s[i-1:i+1]
            if canBreak(prev2):
                dp[i] = dp[i-2]+dp[i-1]
            else:
                if prev2 == "10" or prev2 == "20":
                    dp[i] = dp[i-2]
                elif s[i] == '0':
                    return 0
                else: # >26 or <10 
                    dp[i] = dp[i-1]
        return dp[-1]