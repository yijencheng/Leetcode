# correct, only append left parenthesis(except the first)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # important! otherwise will pop from empty list
        ans = 0
        for i in range(len(s)):
            p = s[i]
            if  p == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0: # the latest index that extra-right happened
                    stack.append(i)
                else:
                    ans = max(ans, i-stack[-1])
        return ans