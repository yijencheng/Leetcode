#sol1: idea

class Solution:
    def checkValidString(self, s: str) -> bool:
        tmp = 0
        for x in s:
            if x == '(' or x == '*':
                tmp += 1
            elif x == ')' :
                tmp -= 1
            if tmp < 0:
                return False
        tmp = 0
        for i in s[::-1]:
            if i == ')' or i == '*':
                tmp += 1
            elif i == '(' :
                tmp -= 1
            if tmp < 0:
                return False
        return True

# sol2
#idea: 
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0
        for ch in s:
            if ch == "(":
                leftMin, leftMax = leftMin+1, leftMax+1
            elif ch ==")":
                leftMin, leftMax = leftMin-1 , leftMax-1
            else:
                leftMax+=1
                leftMin-=1
            
            if leftMax<0:
                return False

            if leftMin<0:
                leftMin = 0  # 

        return leftMin <=0
                
