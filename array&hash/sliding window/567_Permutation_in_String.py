Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

# best
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        d = {}
        l = 0
        for i,ch in enumerate(s2):
            if ch not in counter.keys():
                l = i+1
                d = {}
            else:
                while d.get(ch, 0) >= counter[ch]:
                    if s2[l] in d:
                        d[s2[l]]-=1
                    l+=1
                d[ch] = d.get(ch, 0)+1
                if sum(d.values()) == len(s1):
                    return True
        return False


# add first 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        d = {} #current cumulate count
        l= 0
        for r in range(len(s2)):
            if s2[r] not in s1:
                d = {} 
            else:
                # check + update left
                if d == {}: #the first
                    l = r

                d[s2[r]] = d.get(s2[r], 0) + 1  # update right first, also prevent keyError
                while d[s2[r]] > counter[s2[r]]:
                    d[s2[l]] -=1
                    l+=1
                
                if r-l+1 == len(s1):return True
        return False

# add first (refactor)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        d = {} #current cumulate count
        l= 0
        for r in range(len(s2)):
            if s2[r] not in s1:
                d = {}
                l = r+1
            else:
                # check + update left
                d[s2[r]] = d.get(s2[r], 0) + 1  # update right first, also prevent keyError
                while d[s2[r]] > counter[s2[r]]:
                    d[s2[l]] -=1
                    l+=1
                
                if r-l+1 == len(s1):return True
        return False


# add later
# check + update left >> update right
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        d = {} #current cumulate count
        l= 0
        for r in range(len(s2)):
            if s2[r] not in s1:
                d = {} 
            else:
                if d == {}: # the first
                    l = r
                else:
                    if s2[r] in d: # to prevent keyError
                        while d[s2[r]] == counter[s2[r]]:
                            d[s2[l]] -=1
                            l+=1

                d[s2[r]] = d.get(s2[r], 0) + 1  # to prevent keyError
                if r-l+1 == len(s1):return True
        return False

#correct too
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        d = {}
        l= 0
        for r in range(len(s2)):
            if s2[r] not in counter.keys():
                d = {}
                l = r
            else:
                if s2[l] not in counter.keys():
                    l = r
                d[s2[r]] = d.get(s2[r], 0)+1
                while d[s2[r]] > counter[s2[r]]:
                    d[s2[l]] -=1
                    l+=1
                if r-l+1 == len(s1):return True
        return False

#wrong
- have bug.... (use the wrong key)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = collections.Counter(s1)
        l = 0
        for i, ch in enumerate(s2):
            if ch not in d.keys():
                l=i+1
            elif d[ch] == 0:
                while s2[l]!=ch:
                    d[l]+=1
                    l+=1
                l+=1
            else: #d[ch] >=1
                d[ch] -=1
                if i-l+1 == len(s1):
                    return True
        return False

#wrong
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d, d_origin = collections.Counter(s1), collections.Counter(s1)
        l = 0
        for i, ch in enumerate(s2):
            if ch not in d.keys():
                d = d_origin
                l=i+1
            elif d[ch] == 0:
                while s2[l]!=ch:
                    d[s2[l]]+=1
                    l+=1
                d[s2[l]]+=1 # >>>>>>> actually wrong!!
                l+=1
            else: #d[ch] >=1
                d[ch] -=1
                if i-l+1 == len(s1):
                    return True
        return False


#correct, but code too long
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d, d_origin = collections.Counter(s1), collections.Counter(s1)
        l = 0
        for i, ch in enumerate(s2):
            if ch not in d.keys():
                d = d_origin.copy()
                l=i+1
            elif d[ch] == 0: ## remove a d[ch] in the front
                while s2[l]!=ch:
                    d[s2[l]]+=1
                    l+=1
                l+=1
            else: #d[ch] >=1
                d[ch] -=1
                if i-l+1 == len(s1):
                    return True
        return False

# wrong
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        d = {}
        l= 0
        for r in range(len(s2)):
            if s2[r] not in counter.keys():
                d = {}
                continue
            else:
                if s2[l] not in counter.keys():
                    l = r
                d[s2[r]] = d.get(s2[r], 0)+1
                while d[s2[r]] > counter[s2[r]]:
                    d[s2[l]] -=1
                    l+=1

                if r-l+1 == len(s1):return True
        return False
            
            