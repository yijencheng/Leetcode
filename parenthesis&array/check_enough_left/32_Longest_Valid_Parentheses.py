class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        # ()()
        # (())
        for i in range(len(s)):
            p = s[i]
            if  p == '(':
                stack.append(i)
            else:
                if len(stack) > 0 and s[stack[-1]] == '(':
                    stack.pop()
                    if len(stack) == 0:
                        ans = max(ans, i-(-1))
                    else:
                        ans = max(ans, i-stack[-1])
                else:
                    stack.append(i)
        return ans



# wrong
# idea: stack only store '('
# issue: 
case: "()(())"
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        cur = 0
        # ()()
        # (())
        for i in range(len(s)):
            p = s[i]
            if  p == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    top = stack.pop()
                    if i-top+1 > cur: # contain
                        cur = i-top+1
                    else:
                        cur += (i-top+1) # >>> wrong!
                    ans = max(ans, cur)
                else:
                    cur = 0
        return ans
                    
        