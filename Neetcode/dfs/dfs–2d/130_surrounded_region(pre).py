#correct
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(i,j):
            if i<0 or i == rows or j<0 or j == cols or board[i][j] != "O":return    # change this line
    
            board[i][j] = 'V'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows-1 or j == 0 or j == cols-1) and board[i][j] == "O":
                    dfs(i,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "V":
                    board[i][j] = "O"
                else: #"O" or "X"
                    board[i][j] = "X"
        return board


# wrong, will cause maximum recursion
ex. [[O,O],[O,O]]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(i,j):
            if i<0 or i == rows or j<0 or j == cols or board[i][j] == "X":return
    
            board[i][j] = 'V'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows-1 or j == 0 or j == cols-1) and board[i][j] == "O":
                    dfs(i,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "V":
                    board[i][j] = "O"
                else: #"O" or "X"
                    board[i][j] = "X"
        return board
        