Initial thought:
* For extra right is simple, use a counter where count++ for '(' and count-- for ')'. If count <0 remove ')'
* For extra left, Maybe is possble to record possible index during the loop(?) 


- first time: remove invalid left (but then still may have extra opening bracket)
- second time: looping in reverse order, to remove extra opening bracket

class Solution:
    def minRemoveToMakeValid(self, s) :
        s = list(s)
        s_l = 0
        for i, c in enumerate(s):
            if c == '(':
                s_l+=1
            elif c == ')':
                s_l-=1
            if s_l <0:
                s_l=0
                s[i] = ""
        s_r = 0
        for i in range(len(s)-1, -1,-1):
            if s[i] == ')':
                s_r +=1
            elif s[i] == '(':
                s_r -=1
            if s_r <0:
                s[i] = ""
                s_r = 0
        
        return "".join(s)

            
