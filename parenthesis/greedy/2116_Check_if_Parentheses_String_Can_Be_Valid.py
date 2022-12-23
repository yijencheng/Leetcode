#sol1.
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        leftMin, leftMax = 0,0
        chance = 0 
        for i in range(len(s)):
            if locked[i] == "0":
                leftMin-=1
                leftMax+=1
                chance+=1
                if leftMax <0:
                    return False
                if leftMin <0:
                    leftMin +=2
                    chance-=1
            else: #fixed
                if s[i] == '(':
                    leftMin+=1
                    leftMax+=1
                else:
                    leftMin-=1
                    leftMax-=1

                if leftMax <0:
                    return False
                if leftMin <0:
                    if chance >0:
                        leftMin +=2
                        chance-=1
                    else: # never enter
                        return False
                
        return leftMin == 0

# but actually there is a even cleaner way with needing `chance`
Question: why does chance always > 0 



# my try (wrong)
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        tmp = []
        count = 0
        for ch in s:
            if ch == '(':
                count +=1
            else:
                count-=1
            tmp.append(count)

        max_change = 0
        adopt_change = 0
        for i in range(len(tmp)):
            if i == len(s)-1:
                return abs(tmp[i]) == adopt_change*2

            if tmp[i] < 0:
                required = ceil(abs(tmp[i])/2)

                if locked[i] == '0':
                    max_change+=1
                    if max_change < required:
                        return False
                    adopt_change = max(required, adopt_change)
                elif locked[i] == '1':
                    if max_change < required:
                        print("C", required, i)
                        return False

            
            
                
                
        
            
            