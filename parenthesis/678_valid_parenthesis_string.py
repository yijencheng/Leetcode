



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