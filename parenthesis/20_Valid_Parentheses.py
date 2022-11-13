

#wrong!!!
class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        for ch in s:
            if ch in "({[":
                sk.append(ch)
            else:
                if ch !=sk.pop():
                    return False
                
        return True if len(sk) == 0 else False

#edge: 
- ]
- [[]]}

class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        d={
            "(":")",
            "{":"}",
            "[":"]",
        }
        for ch in s:
            if ch in "({[":
                sk.append(ch)
            else:
                if len(sk)==0 or ch!= d[sk.pop()]:
                    return False
                
        return True if len(sk) == 0 else False