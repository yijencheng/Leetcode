1.(最多可以再幾個右）Have two counters one counter (cmax) for counting the maximum number of right braces we can accommodate with current left braces and stars.
2.(最少還需要幾個右）Have a second counter(cmin) which represents the minimum number of right braces that must be there further to make sure the whole string is valid(this number can’t be negative, so if it becomes negative then we put it to zero.
3.At any time, if cmax becomes negative, it means we can’t accommodate current right braces with current left braces and stars. So, we return false.
4.In the end if cmin is positive then it means that at least there should be a cmin number of right braces to make sure the overall string is valid. So, we check whether cmin is zero or not and return the answer

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
            
            if leftMax<0: # check first, if >0, means we still have space to fix leftMin.
                return False

            if leftMin<0:
                leftMin +=1 ## change from ")" -> "*"

        return leftMin == 0

# The reason why no needing to check `chance`, is because there is always enough '*' for left to change
# Proof: 
# everytime '*' is encountered, the difference between min & max by right will incr by 2. 
# However, if leftMin<0, we will do adjustion, which means the difference will only have one. Every '*' provide two chance for leftMin<0 to adjust

# 2.What if there is more '<0' cases than it can fixed? In that case, leftMin will alrdy be equal to leftMax, hence the `leftMax<0` check will fail. 

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

