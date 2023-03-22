# Hint: 
# two possibility:
# - extra right: should be removed
# - extra left(the one that left in the stack): should be removed

Sol1: 
- extra right: 
class Solution:
    def minRemoveToMakeValid(self, s) :
        stack=[]
        split_str=list(s)
        for i in range(len(s)):
            if s[i]=='(':
                # if current char is '(' then push it to stack
                stack.append(i)
            elif s[i]==')':
                # if current char is ')' then pop top of the stack
                if len(stack) !=0:
                    stack.pop()
                else:
                    # extra right 
                    split_str[i]=""
        
        for i in stack: # extra left
            split_str[i]=""
        return '' .join(split_str)


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
        print(s)
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




class Solution:
    def minSwaps(self, s: str) -> int:
       l, r = 0, len(s)-1
       s_l, s_r = 0,0 
       swap = 0
       while l<r:
           while s_l>=0:
               if s[l] == '[':
                   s_l+=1
                else:
                    s_l-=1
            while s_r>=0:
                if s[r] == '[':
                   s_r+=1
                else:
                    s_r-=1
            swap+=1
            s_l,s_r = 0,0 
            l,r = l+1, r-1
        return swap
            
