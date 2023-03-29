# Hint: 
# two possibility:
# - extra right: should be removed
# - extra left(the one that remain in the stack): should be removed

previous question: p1963

# More comprehensive
# right:
# - valid right: match with left
# - extra right: remove current parenthesis

# Q. why do we need stack? 
# A. Originally only leftCount is needed, however since there might be extra left, we need to remember the previous index. 

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
                else: # extra right 
                    split_str[i]=""
        
        for i in stack: # extra left
            split_str[i]=""
        return '' .join(split_str)
