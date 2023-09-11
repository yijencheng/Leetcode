
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        found = [False]
        def dfs(i,j, wordPtr):
            if i<0 or i >= rows or j<0 or j>=cols or board[i][j] == "":return

            if board[i][j] != word[wordPtr]:return
            
            if wordPtr == len(word)-1:
                found[0] = True
                return

            
            #match
            tmp = board[i][j]
            board[i][j] = ""
            dfs(i+1,j, wordPtr+1)
            dfs(i-1,j, wordPtr+1)
            dfs(i,j+1, wordPtr+1)
            dfs(i,j-1, wordPtr+1)
            board[i][j] = tmp
        
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,0)
                if found[0] == True:return True
        return found[0]


# Daily log
## 2022.11.09
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        found = [False]
        def dfs(i,j,word):
            if word == "": 
                found[0] = True
                return

            if i<0 or i>=rows or j<0 or j>=cols or board[i][j] == "":return
            if board[i][j] != word[0]:
                return
            
            tmp = board[i][j]
            board[i][j] = ""
            dfs(i+1, j, word[1:])
            dfs(i-1, j, word[1:])
            dfs(i, j+1, word[1:])
            dfs(i, j-1, word[1:])
            board[i][j] = tmp
        
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,word)
        return found[0]
            
            
            