Prvious: p912
# 
class Solution:
    def minInsertions(self, s: str) -> int:
        l = 0
        ret = 0
        i=0
        while i < len(s):
            p = s[i]
            if p == '(':
                l +=1
            else:
                if i+1<len(s) and s[i+1] == ')':
                    l-=1
                    i+=1
                else: # ()(
                    ret+=1
                    l-=1
                if l<0:
                    ret+=1
                    l=0
            i+=1
        ret+=l*2
        return ret
    

# correct
class Solution:
    def minInsertions(self, s: str) -> int:
        l = 0
        tmp = 0
        ret = 0
        for i,p in enumerate(s):
            if p == '(':
                if tmp == 1:
                    tmp = 0
                    if l > 0:
                        ret +=1
                        l-=1
                    else: # l == 0:
                        ret+=2
                l +=1
            else:
                if tmp == 0:
                    tmp+=1
                else: # tmp=1
                    tmp = 0
                    l-=1
                    if l<0:
                        ret+=1
                        l=0
            
        if l > 0:
            ret+=l*2-tmp
        elif tmp==1:
            ret+=2
        return ret


# wrong!!!! 
# Case:
# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. 
# We need to add one more ')' at the end of the string to be "(())))" which is balanced.
class Solution:
    def minInsertions(self, s: str) -> int:
        l=0
        extra_right = 0
        for p in s:
            if p == '(':
                l+=2 # one left equal to two right
            else:
                if l > 0:
                    l-=1
                else:
                    extra_right+=1
        left_needed = (extra_right + 1)//2
        right_needed = l*2 + extra_right%2
        return left_needed + right_needed


# wrong!!!! 
# Case: "(((()(()((())))(((()())))()())))(((()(()()((()()))"
class Solution:
    def minInsertions(self, s: str) -> int:
        l=0
        extra_left = 0
        extra_right = 0
        for i, p in enumerate(s):
            if p == '(':
                if i>0 and s[i-1] == ')' and l > 0: #important
                    extra_left+=l
                    l=0
                l+=2 # one left equal to two right
            else:
                if l > 0:
                    l-=1
                else:
                    extra_right+=1
        extra_left += l # important 
        print(extra_left, extra_right)
        left_needed = (extra_right + 1)//2
        right_needed = extra_left + extra_right%2
        return left_needed + right_needed
    