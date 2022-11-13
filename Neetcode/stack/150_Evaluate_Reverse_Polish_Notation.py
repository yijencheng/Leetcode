class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in "+-*/":
                stack.append(int(tok))
                continue
            r = stack.pop()
            l = stack.pop()
            result = self.calc(l,r,tok)
            stack.append(result)
        return stack[0]
    def calc(self, l,r,opt):
        if opt == '+':return l+r
        if opt == '-':return l-r
        if opt == '*':return l*r
        if opt == '/':
            if r == 0:
                print("error")
                return -1
            return int(l/r)