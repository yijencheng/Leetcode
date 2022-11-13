#pass, better
def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# pass, can
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start<end:
            if not s[start].isalnum():
                start+=1
            elif not s[end].isalnum():
                end-=1
            else:
                if s[start].lower()!=s[end].lower():
                    return False
                start+=1
                end-=1
        return True

#pass, but not good
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start<end:
            if not s[start].isalnum():
                start+=1
                continue
            if not s[end].isalnum():
                end-=1
                continue
            if s[start].lower()!=s[end].lower():
                return False
            start+=1
            end-=1
        return True