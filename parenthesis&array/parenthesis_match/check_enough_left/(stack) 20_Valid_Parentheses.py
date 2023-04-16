class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d={
            "(":")",
            "{":"}",
            "[":"]",
        }
        for ch in s:
            if ch in ["(", "{", "["]:
                stack.append(ch)
            else:
                if len(stack)==0 or ch!= d[stack.pop()]:
                    return False
                
        return len(stack) == 0 