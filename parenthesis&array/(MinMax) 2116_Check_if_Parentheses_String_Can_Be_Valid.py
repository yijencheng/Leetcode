# wrong!!!!
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        leftMin, leftMax = 0,0
        for i in range(len(s)):
            if locked[i] == "1":
                if s[i] == '(':
                    leftMin+=1
                    leftMax+=1
                else:
                    leftMin-=1
                    leftMax-=1
                
                if leftMin<0: ## cause fixed. But this lead to the wrong answer, since previous pos still may have the change to cahnge from ')' to '('
                    return False
            else: #"0"
                leftMin-=1
                leftMax+=1

                if leftMin<0:
                    leftMin +=2
            
            if leftMax <0:
                return False

        return leftMin == 0

# there are two ways to solve the issue:
# first is to add a `change` variable, which shows how many available position until now that can be changed from '(' to ')'
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        leftMin, leftMax = 0,0
        chances = 0
        for i in range(len(s)):
            if locked[i] == "1":
                if s[i] == '(':
                    leftMin+=1
                    leftMax+=1
                else:
                    leftMin-=1
                    leftMax-=1
                
                if leftMin<0:
                    if chances == 0:
                        return False
                    else:
                        leftMin +=2
                        chances-=1
            else: #"0"
                leftMin-=1
                leftMax+=1
                chances +=1

                if leftMin<0:
                    leftMin +=2
                    chances-=1
            
            if leftMax <0:
                return False

        return leftMin == 0


# but actually there is a even cleaner way without needing `chance`. There is alwas enough '*' for left to change
# *** proof: if there chance equals 0, means every position is fixed, then leftMax = leftMin. In this case ,leftMax <0 will always failed. 
# Ex. "(*))", index=2
# 1st: leftMin, leftMax = 1 1 >> after check remain to 1,1
# 2nd: leftMin, leftMax = 0 2 >> after check remain to 0,2
# 3rd: leftMin, leftMax = -1 1 >> after check remain to 1,1 
# 4th
# **** In the 3rd round, though s[i] is fixed, since there is still one '*' chance left, it don't need to early return false.
# **** Noted that after they useout the `chance`, leftMin & leftMax become the same value.
# 
# So if you switch the check order, the answer will be wrong 



Question: why does chance always > 0 
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        leftMin, leftMax = 0,0
        for i in range(len(s)):
            if locked[i] == "0":
                leftMin-=1
                leftMax+=1
            elif locked[i] == "1":
                if s[i] == '(':
                    leftMin+=1
                    leftMax+=1
                else:
                    leftMin-=1
                    leftMax-=1
                
            if leftMax <0:
                return False
            if leftMin <0:                
                leftMin +=2

        return leftMin == 0
            
                