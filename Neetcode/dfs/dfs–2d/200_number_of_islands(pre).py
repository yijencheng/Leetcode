#similar 
from jmespath import search


- Number of Enclaves
- Surrounded Regions
- Word Search
- Smallest Rectangle
- Enclosing Black Pixels

#correct
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i, j-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    ans+=1
                    dfs(i, j)
        return ans

#wrong
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        
        def dfs(i,j):
            if i<0 or i>rows or j<0 or j>cols or grid[i][j] == '0':
                return
            grid[i][j] = 0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i, j-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    ans+=1
                    dfs(i, j)
        return ans

        
                    