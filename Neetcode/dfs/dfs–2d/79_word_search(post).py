class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        find = False
        def dfs(i,j, wordPtr):
            if i<0 or i >= rows or j<0 or j>=cols or board[i][j] == "": return

            #not match
            if board[i][j] != word[wordPtr]:return
            
            if wordPtr == len(word)-1:
                return True
            
            #match
            tmp = board[i][j]
            board[i][j] = ""
            ans = (dfs(i+1,j, wordPtr+1) or 
            dfs(i-1,j, wordPtr+1) or 
            dfs(i,j+1, wordPtr+1) or 
            dfs(i,j-1, wordPtr+1))

            board[i][j] = tmp
            return ans
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False