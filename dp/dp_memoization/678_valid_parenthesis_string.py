* https://leetcode.com/problems/valid-parenthesis-string/discuss/1542811/O(3n)-Brute-force-solution-to-O(n2)-memoization-solution
* https://www.youtube.com/watch?v=QhPdNS143Qg


#without memo
class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(index, oCount):
            if oCount < 0:return False
            if index == sLen: #the last/leaf of the tree
                return oCount == 0
            
            if s[index] == '(':
                return dfs(index+1, oCount + 1)
            elif s[index] == ')':
                return  dfs(index+1, oCount-1)
            else: #'*'
                return dfs(index+1, oCount + 1) or dfs(index+1, oCount - 1) or dfs(index+1, oCount)

        sLen = len(s)
        return dfs(0, 0)


#with memo
class Solution:
    def checkValidString(self, s: str) -> bool:
        mem = {}
        def dfs(index, oCount):
            if oCount < 0:return False
            if index == sLen: #the last/leaf of the tree
                return oCount == 0
            
            if (index,oCount) in mem:
                return mem[(index,oCount)]
            
            if s[index] == '(':
                mem[(index, oCount)] =  dfs(index+1, oCount + 1)
            elif s[index] == ')':
                mem[(index, oCount)] =  dfs(index+1, oCount - 1)
            else: #'*'
                mem[(index, oCount)] =  dfs(index+1, oCount + 1) or dfs(index+1, oCount - 1) or dfs(index+1, oCount)
            return mem[(index, oCount)]

        sLen = len(s)
        return dfs(0, 0)