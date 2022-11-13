https://www.youtube.com/watch?v=QhPdNS143Qg
https://www.youtube.com/watch?v=ReR0bp9cAtc



Why cant I just have leftMax >0 ?
* , ex. '(((', 

leftMin: 

(*)) >> 
* leftMin: 1 0 -1(0) -1(0) 

# wrong!!! (2 error)
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0
        for ch in s:
            if s == "(":
                leftMin, leftMax = leftMin+1 , leftMax+1
            elif s ==")":
                leftMin, leftMax = leftMin-1 , leftMax-1
            else:
                leftMax+=1
                leftMin-=1
                if leftMax<0:return False
                if leftMin<0:leftMin=0
        return leftMin == 0
                


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
                leftMin=0

        return leftMin == 0
                
