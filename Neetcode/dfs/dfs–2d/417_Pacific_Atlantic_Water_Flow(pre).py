class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c ==0:
                    dfs(r, c, pac, heights[r][c])
                if r == ROWS-1 or c == COLS-1:
                    dfs(r, c, atl, heights[r][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


# cool tricks, only use one set()
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c ==0:
                    dfs(r, c, pac, heights[r][c])
                if r == ROWS-1 or c == COLS-1:
                    dfs(r, c, atl, heights[r][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


# cool tricks, only use one set()
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        ans = []
        m = [[0]*cols for i in range(rows)]
        s = set()
        def dfs(i,j,flag, prevHeight):
            #0, same flag, different flag, -1
            if i<0 or i>=rows or j<0 or j>=cols or m[i][j] == flag:return
            if heights[i][j] < prevHeight: return

            if m[i][j]*flag == 6:
                s.add((i,j))

            m[i][j] = flag
            dfs(i+1,j,flag, heights[i][j])
            dfs(i-1,j,flag, heights[i][j])
            dfs(i,j+1,flag, heights[i][j])
            dfs(i,j-1,flag, heights[i][j])


        # -3: float to left
        # -2: float to right
        # -1: answer
        for i in range(rows):
            for j in range(cols):
                # only dfs for four borders
                if i == 0 or j == 0:
                    dfs(i,j,-3, heights[i][j])
                if i==rows-1 or j == cols-1:
                    dfs(i,j,-2, heights[i][j])
        
        for elem in s:
            ans.append([elem[0],elem[1]])
        return ans
