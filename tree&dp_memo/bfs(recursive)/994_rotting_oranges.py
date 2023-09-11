#wrong
* the last rotten orange will do ans+=1, thoguh all of its neighbor is rotten
* 如果沒辦法把全部橘子變成 rotten，還是會回傳answer
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        q = []
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        while q:
            for i in range(len(q)):
                r,c = q.pop(0)
                if r-1>=0 and grid[r-1][c] == 1:
                    fresh-=1
                    grid[r-1][c]=2
                    q.append((r-1,c))
                if r+1<rows and grid[r+1][c] == 1:
                    fresh-=1
                    grid[r+1][c]=2
                    q.append((r+1,c))
                if c-1>=0 and grid[r][c-1] == 1:
                    fresh-=1
                    grid[r][c-1]=2
                    q.append((r,c-1))
                if c+1<cols and grid[r][c+1] == 1:
                    fresh-=1
                    grid[r][c+1]=2
                    q.append((r,c+1))
            ans +=1 
        return ans
    
            

            
            
        
                    
        