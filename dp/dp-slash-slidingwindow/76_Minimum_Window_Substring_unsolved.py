#wrong 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt, ds = collections.Counter(t),  collections.Counter(s)
    
        # check if ans is possible
        for ch in t:
            if ds[ch]<dt[ch]:return ""

        l,r = 0, len(s)-1
        def dp(l,r):
            if s[l] not in t:
                return dp(l+1, r)
            if s[r] not in t:
                return dp(l, r-1)
            c  = collections.Counter(s[l:r+1])

            if c[s[l]] == dt[s[l]] or c[s[r]]==dt[s[r]]: #cannot have ans less than this len
                return s[l:r+1]
            
            if c[s[l]]>dt[s[l]]:
                left = dp(l+1, r)
            if c[s[r]]>dt[s[r]]:
                right = dp(l, r-1)
            return left if len(left)<len(right) else right
            
        return dp(l,r)
***
- line18. should be `and` not `or`
- line21-24, left & right is not defined beforehand
***


#TLE
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt, ds = collections.Counter(t),  collections.Counter(s)
    
        # check if ans is possible
        for ch in t:
            if ds[ch]<dt[ch]:return ""

        l,r = 0, len(s)-1
        def dp(l,r):
            if s[l] not in t:
                return dp(l+1, r)
            if s[r] not in t:
                return dp(l, r-1)
            c  = collections.Counter(s[l:r+1])

            if c[s[l]] == dt[s[l]] and c[s[r]]==dt[s[r]]: #cannot have ans less than this len
                return s[l:r+1]
            
            left, right = None, None
            if c[s[l]]>dt[s[l]]:
                left = dp(l+1, r)
            if c[s[r]]>dt[s[r]]:
                right = dp(l, r-1)
            
            if not left:return right
            elif not right:return left
            else:
                return left if len(left)<len(right) else right
            
        return dp(l,r)



#correct
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not t or not s:
            return ""

        dt = Counter(t)
        l, r = 0, 0

        # unique characters in t are present in the current window in its desired frequency.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}
        ans = ""

        for r, ch in enumerate(s):
            window_counts[ch] = window_counts.get(ch, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if ch in dt and window_counts[ch] == dt[ch]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == len(dt):
                if ans == "" or r - l + 1 < len(ans):
                    ans = s[l:r+1]

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[s[l]] -= 1
                if ch in dt and window_counts[s[l]] < dt[s[l]]:
                    formed -= 1

                l += 1    

        return ans
            