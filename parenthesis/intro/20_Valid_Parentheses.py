
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d={
            "(":")",
            "{":"}",
            "[":"]",
        }
        for ch in s:
            if ch in d.keys():
                stack.append(ch)
                continue

            if len(stack)==0 or ch!= d[stack.pop()]:
                return False
                
        return len(stack) == 0 
        