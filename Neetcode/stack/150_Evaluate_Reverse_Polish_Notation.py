class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in "+-*/":
                stack.append(int(tok))
            else:
                b, a = stack.pop(), stack.pop() # need to add empty check
                if tok == "+":
                    stack.append(a+b)
                if tok == "-":
                    stack.append(a-b)
                if tok == "*":
                    stack.append(a*b)
                if tok == "/":
                    stack.append(a//b)
        return stack[0]