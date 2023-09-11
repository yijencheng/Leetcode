[a,b]
[b,a]
ababababa
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        ## 找i, j 位子上是否等於word[ptr]
        ## 是：上下左右是否「有任何一個」等於word[ptr+1]，直到ptr == len(word)-1
        ## 不是：return
        def dfs(i, j, ptr):
            if i<0 or i>=rows or j<0 or j>= cols:
                return
            if word[ptr]!=board[i][j]:
                return
            ## 等於
            if ptr == len(word)-1:
                return True

            return dfs(i+1, j, ptr+1) or dfs(i, j+1, ptr+1) or dfs(i-1, j, ptr+1) or dfs(i, j-1, ptr+1)
            # tmp = board[i][j]
            # board[i][j] = ""
            # ans = dfs(i+1, j, ptr+1) or dfs(i, j+1, ptr+1) or dfs(i-1, j, ptr+1) or dfs(i, j-1, ptr+1)
            # board[i][j] = tmp
            # return ans
            

        ptr = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[ptr]:
                    dfs(i,j, ptr)