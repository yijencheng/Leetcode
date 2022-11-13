#better
class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0)+1
            if d[ch] == 2:
                longest+=2
                del d[ch]
        if d.keys():
            longest+=1
        return longest



#wrong !!! 
ccc >> 3
class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        has_odd = False
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0)+1
        
        for k,freq in d.items():
            if freq%2 == 0:
                longest +=freq
            if freq%2 == 1:
                has_odd = True 
        return longest+1 if has_odd else longest

#wrong answer!!
class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        odd_max = 0
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0)+1
        
        for k,freq in d.items():
            if freq%2 == 0:
                longest +=freq
            if freq%2 == 1:
                odd_max = max(odd_max, freq)
        return longest+odd_max


class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        has_odd = False
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0)+1
        
        for k,freq in d.items():
            if freq%2 == 0:
                longest +=freq
            if freq%2 == 1:
                has_odd = True
                longest += freq-1
        return longest+1 if has_odd else longest