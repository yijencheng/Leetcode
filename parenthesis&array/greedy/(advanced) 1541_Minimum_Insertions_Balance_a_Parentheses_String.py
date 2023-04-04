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
                # valid case
                if i+1<len(s) and s[i+1] == ')':
                    l-=1
                    i+=1
                else: # invalid case, greedly fix (by adding one more right)
                    ret+=1
                    l-=1

                if l<0:
                    ret+=1
                    l=0
            i+=1
        ret+=l*2
        return ret