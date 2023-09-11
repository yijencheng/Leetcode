#wrong!(see the below example)
# def add(num):
#     num+=1

# num = 5
# add(num)
# print(num) # 5 not 6


#correct
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==0:return 0
            elif grid[i][j]!=1:
                ##raise error
                return 0
            grid[i][j]=0
            return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)

        for i in range(rows):
            for j in range(cols):
                maxArea = max(maxArea, dfs(i,j))
        return maxArea


#Hence, for immutable type, we should explicit return state !!!!
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        
        def dfs(i,j,area):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!=1:
                return
            
            area +=1
            grid[i][j] = 0
            dfs(i+1, j, area)
            dfs(i, j+1, area)
            dfs(i-1, j, area)
            dfs(i, j-1, area)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j,area)
                    ans = max(ans,area)
        return ans


            