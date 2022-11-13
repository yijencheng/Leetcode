from unittest import case


Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.



special case
"ADOBECODEBANC"
"ABC"
===
"aa"
"aa"
====
"aab"
"aab"
====
"aBAbaAabBbA"
"bbA"


"bbcbcbccbbaaabacb"
"abca"

# passed
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = 0
        target = collections.Counter(t) 
        num_left = len(target.keys()) # calculate # of string still need to be matched
        
        cur = {}
        shortest = s
        found = False
        for r in range(len(s)):
            cur[s[r]]  = cur.get(s[r], 0)+1
            if cur[s[r]] != target[s[r]]:
                continue
            num_left-=1
            if num_left != 0:continue
                    
            while l < r and cur[s[l]] > target[s[l]]:
                cur[s[l]]-=1
                l+=1
            shortest = s[l:r+1] if r-l+1 < len(shortest) else shortest
            found = True
            # print("before:",l,r,s[l:r+1], num_left)

            while l < r and num_left == 0:
                cur[s[l]]-=1
                if cur[s[l]] < target[s[l]]:num_left +=1
                l+=1
            # print("after:",l,r,s[l:r+1], num_left)

        return shortest if found else ""
              
              
#reference solution!
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

      
        
# TLE
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = 0
        target = collections.Counter(t) 
        num_left = len(target.keys()) # calculate # of string still need to be matched
        
        cur = {}
        shortest = s
        found = False
        for r in range(len(s)):
            if s[r] not in t:
                continue
            elif num_left >= 2: # not the last
                cur[s[r]]  = cur.get(s[r], 0)+1
                if cur[s[r]] == target[s[r]]:
                    num_left -=1
            else: # 1 number left 
                cur[s[r]]  = cur.get(s[r], 0)+1
                if cur[s[r]] != target[s[r]]:
                    continue
                else: # cur[s[r]] == target[s[r]], 超重要！need to be exactly equal
                    num_left-=1
                    
                while l < r and (s[l] not in t or cur[s[l]] > target[s[l]]):
                    if s[l] in t:
                        cur[s[l]]-=1
                    l+=1
                shortest = s[l:r+1] if r-l+1 < len(shortest) else shortest
                found = True
                print("before:",l,r,s[l:r+1], num_left)
                
                while l < r and num_left == 0:
                    if s[l] not in t:continue
                    cur[s[l]]-=1
                    
                    if cur[s[l]] < target[s[r]]:num_left +=1
                    l+=1
                print("after:",l,r,s[l:r+1], num_left)

        return shortest if found else ""
                    
                    
        
#wrong!
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = 0
        target = collections.Counter(t) 
        num_left = len(t) # calculate # of string still need to be matched
        
        cur = {}
        shortest = s
        found = False
        for r in range(len(s)):
            if s[r] not in t: # 1st or middle
                continue
            elif num_left >= 2: # not the last
                cur[s[r]]  = cur.get(s[r], 0)+1
                if cur[s[r]] == target[s[r]]:
                    num_left -=1
            else: # 1 number left 
                cur[s[r]]  = cur.get(s[r], 0)+1
                if cur[s[r]] != target[s[r]]:
                    continue
                else: # cur[s[r]] == target[s[r]], 超重要！need to be exactly equal
                    num_left-=1

                shortest = s[l:r+1] if r-l+1 < len(shortest) else shortest
                found = True
                print("before:", l,r,s[l:r+1], num_left)
                
                #update s.t cur[s[r]] not exceed 
                while l < r and cur[s[r]] == target[s[r]]:
                    if s[l] in t:
                        cur[s[l]]-=1
                    if cur[s[l]] <target[s[l]]:num_left +=1
                    l+=1

                while l < r and cur[s[l]] > target[s[r]] or (s[l] not in t):
                    if s[l] in t:
                        cur[s[l]]-=1
                    l+=1

                print("after:",l,r,s[l:r+1], num_left)

        return shortest if found else ""
                    
        

# wrong. 題目可以允許window包含某個字母比t裡面的更多，因此用 while cur[s[r]] < 0 會錯
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = 0
        cur, target = collections.Counter(t), collections.Counter(t) 
        num_left = len(t) # calculate number of string still need to be matched
        
        shortest = s
        found = False
        for r in range(len(s)):
            if s[r] not in t: # 1st or middle
                continue
            else: # might be 1st, middle, last
                cur[s[r]] -=1
                num_left -=1
                # remain valid
                while cur[s[r]] < 0 or s[l] not in t: # ********important logic
                    if s[l] in t:
                        cur[s[l]]+=1
                        num_left+=1
                    l+=1 # should put outside!
                if num_left == 0: #last
                    shortest = s[l:r+1] if r-l+1 < len(shortest) else shortest
                    found = True

        return shortest if found else ""
                    
        