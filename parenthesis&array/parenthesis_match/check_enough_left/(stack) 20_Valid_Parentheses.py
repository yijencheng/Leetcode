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



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def isMatch(l,r):
            if l == '(':
                return r == ')'
            elif l == '{':
                return r == '}'
            elif l == '[':
                return r == ']'
            return False

        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                elif not isMatch(stack.pop(),ch):
                    return False
                
        return len(stack) == 0 
        