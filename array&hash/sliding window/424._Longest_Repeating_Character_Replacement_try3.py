# correct, without sliding window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        for i in range(len(s)):
            ptr = i
            d = {}
            while ptr >=0:
                d[s[ptr]] = d.get(s[ptr], 0)+1
                if (i-ptr+1) - max(d.values()) > k:
                    break
                ptr-=1
            longest = max(longest, i-ptr)
        return longest


# sliding window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        d = {}
        l = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0)+1
            while (i-l+1) - max(d.values()) > k:
                d[s[l]] -=1
                l+=1
            longest = max(longest, i-l+1)
        return longest


# correct, but not suggest
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        longest = 0
        l=0
        # for new elem, two possibility
        # - not the max: will take extra k
        # - equals the max: length +=1
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0)+1
            if s[i] == max(d.values()):
                longest = max(longest, i-l+1)
            else:
                while (i-l+1) - max(d.values()) > k:
                    d[s[l]]-=1
                    l+=1
                longest = max(longest, i-l+1)
        return longest
