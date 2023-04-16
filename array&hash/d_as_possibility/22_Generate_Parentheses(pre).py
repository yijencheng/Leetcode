class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        d = defaultdict(list) # key: #open parenthesis, value: possibility
        for i in range(2*n):
            if not d.keys():
                d[1].append("(")
            else:
                tmp = defaultdict(list)
                for k, values in d.items():
                    for v in values:
                        if k > 0:
                            # opening
                            tmp[k+1].append(v+'(')
                            # closing
                            tmp[k-1].append(v+')')
                        elif k == n:
                            tmp[k-1].append(v+')')
                        else: # k == 0
                            tmp[k+1].append(v+'(')
                d = tmp
        return d[0]