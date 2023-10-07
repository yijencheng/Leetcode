class Solution:
    def repeatedCharacter(self, s: str) -> str:
        sets = set()
        for ch in s:
            if ch in sets:
                return ch
            sets.add(ch)
        return False
    