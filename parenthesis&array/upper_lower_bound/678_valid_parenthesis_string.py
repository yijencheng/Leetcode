# sol1
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0
        for ch in s:
            if ch == "(":
                leftMin+=1
                leftMax+=1
            elif ch ==")":
                leftMin-=1
                leftMax-=1
            else:
                leftMin-=1 # fill as right
                leftMax+=1 # fill as left
            
            if leftMax<0:
                return False

            if leftMin<0:
                leftMin +1 ## change from ")" -> "*"

        return leftMin == 0

# The reason why no needing to check `chance`, is because there is always enough '*' for left to change
# Proof: 
# everytime '*' is encountered, the difference between min & max by right will incr by 2. 
# However, if leftMin<0, we will do adjustion, which means the difference will only have one. Every '*' provide two chance for leftMin<0 to adjust
# What if there is more '<0' cases than it can fixed? In that case, leftMin will alrdy be equal to leftMax, hence the `leftMax<0` check will fail. 

#sol2: left to right + right to left

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



                



(a(b(c))

