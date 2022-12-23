# TLE
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tries = {}
        rows, cols = len(board), len(board[0])
        ans = []
        
        # build tries
        for w in words:
            ptr = tries
            for c in w:
                if c not in ptr:
                    ptr[c] = {}
                ptr = ptr[c]
            ptr['$'] = w
        
        def dfs(i,j,tries_level):
            if i >= rows or i < 0 or j >=cols or j <0 or board[i][j] is None:return
            if board[i][j] not in tries_level:return
            
            #match
            if '$' in tries_level[board[i][j]]:
                ans.append(tries_level[board[i][j]]['$'])
                tries_level[board[i][j]].pop('$')
            
            tries = tries_level[board[i][j]]
            
            tmp = board[i][j]
            board[i][j] = None
            dfs(i+1, j, tries)
            dfs(i-1, j, tries)
            dfs(i, j+1, tries)
            dfs(i, j-1, tries)
            board[i][j] = tmp

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,tries)
                    
        return ans