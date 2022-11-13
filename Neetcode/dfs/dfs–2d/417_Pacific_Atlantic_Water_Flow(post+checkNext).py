* 先還是後？ 見problem98

# pass, but slow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        ans = []
        d = {}
        # target = "Pac", "Atl"
        def dfs(prev, i,j, target):
            if i<0 or j<0:
                return target == "Pac"
            elif i>=rows or j>=cols:
                return target == "Atl"

            if heights[i][j] == "":return False
            if prev < heights[i][j]:return False

            cur = heights[i][j]
            heights[i][j] = ""
            valid = dfs(cur, i-1, j, target) or dfs(cur, i, j-1, target) or dfs(cur, i, j+1, target) or dfs(cur, i+1, j, target)
            heights[i][j] = cur
            return valid

        for i in range(rows):
            for j in range(cols):
                pac = dfs(float('inf'), i,j, "Pac")
                atl = dfs(float('inf'), i,j, "Atl")
                if pac and atl:
                    ans.append([i,j])

        return ans

# seemed correct, but TLE
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        ans = []
        d = {}
        # target = "Pac", "Atl"
        def dfs(i,j, target):
            if i<0 or j<0:
                return target == "Pac"
            elif i>=rows or j>=cols:
                return target == "Atl"
            elif heights[i][j] == "":return True

            cur = heights[i][j]
            heights[i][j] = ""
            up, down, l,r = True,True,True,True
            if i>0 and (heights[i-1][j] == "" or heights[i-1][j] > cur):
                up = False
            if i<rows-1 and (heights[i+1][j] == "" or heights[i+1][j] > cur):
                down = False
            if j>0 and (heights[i][j-1] == "" or heights[i][j-1] > cur):
                l = False
            if j<cols-1 and (heights[i][j+1] == "" or heights[i][j+1] > cur):
                r = False
            valid = (up and dfs(i-1, j, target)) or (l and dfs(i, j-1, target)) or (r and dfs(i, j+1, target)) or (down and dfs(i+1, j, target))

            # print(i,j,target, up,down,l,r, valid)
            heights[i][j] = cur
            return valid

        for i in range(rows):
            for j in range(cols):
                pac = dfs(i,j, "Pac")
                atl = dfs(i,j, "Atl")
                if pac and atl:
                    ans.append([i,j])

        return ans


# almost right, but 如果是向左留，先向右繞一圈，就會漏掉。因此會需要記住每個地點是只能到pac, 只能到atl還是都可以
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        ans = []
        d = {}
        # target = "Pac", "Atl", "All"
        def dfs(i,j, target):
            if i<0 or i>=rows or j<0 or j>=cols or heights[i][j] == "":return True

            cur = heights[i][j]
            heights[i][j] == ""
            up, down, l,r = True,True,True,True
            if i>0 and heights[i-1][j] > cur:
                up = False
            if i<rows-1 and heights[i+1][j] > cur:
                down = False
            if j>0 and heights[i][j-1] > cur:
                l = False
            if j<cols-1 and heights[i][j+1] > cur:
                r = False
            
            valid = False
            if target == "Pac":
                valid = (up and dfs(i-1, j, "Pac")) or (l and dfs(i, j-1, "Pac")) 
            elif target == "Atl":
                valid = (r and dfs(i, j+1, "Atl")) or (down and dfs(i+1, j, "Atl")) 
            else:
                pac = (up and dfs(i-1, j, "Pac")) or (l and dfs(i, j-1, "Pac")) 
                atl = (r and dfs(i, j+1, "Atl")) or (down and dfs(i+1, j, "Atl"))
                valid = pac and atl
                if valid:ans.append([i,j])
                print(i,j,target, up,down,l,r, pac, atl)
            heights[i][j] = cur
            return valid
            
    
        for i in range(rows):
            for j in range(cols):
                if i==2 and j == 1:
                    dfs(i,j, "All")

        return ans

# wrong
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        ans = []
        # "": current dfs
        # T/F: checked before, [Success, Fail]
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or heights[i][j] == "":return True
            if heights[i][j] == "T":return True
            if heights[i][j] == "F":return False

            cur = heights[i][j]
            heights[i][j] == ""
            up, down, l,r = True,True,True,True
            if i>0 and (heights[i-1][j] == 'F' or heights[i-1][j] > cur):
                up = False
            if i<rows-1 and (heights[i+1][j] == 'F' or heights[i+1][j] > cur):
                down = False
            if j>0 and (heights[i][j-1] == 'F' or heights[i][j-1] > cur):
                l = False
            if j<cols-1 and (heights[i][j+1] == 'F' or heights[i][j+1] > cur):
                r = False
            print(i,j,heights)
            
            if up and down and l and r and dfs(i-1, j) and dfs(i, j-1) and dfs(i+1, j) and dfs(i, j+1):
                heights[i][j] = 'T'
                ans.append([i,j])
                return True
            else:
                heights[i][j] = 'F'
                return False
    
        for i in range(rows):
            for j in range(cols):
                dfs(i,j)

        return ans
# wrong
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        ans = []
        # "": current dfs
        # T/F: checked before, [Success, Fail]
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or heights[i][j] == "":return True
            if heights[i][j] == "T":return True
            if heights[i][j] == "F":return False

            cur = heights[i][j]
            heights[i][j] == ""
            up = (i==0) or heights[i-1][j] <= cur
            down = (i==rows-1) or heights[i+1][j]<= cur
            l = (j==0) or heights[i][j-1] <= cur
            r = (j==cols-1) or heights[i][j+1]<= cur
            
            if up and down and l and r and dfs(i-1, j) and dfs(i, j-1) and dfs(i+1, j) and dfs(i, j+1):
                heights[i][j] = 'T'
                ans.append([i,j])
                return True
            else:
                heights[i][j] = 'F'
                return False
    
        for i in range(rows):
            for j in range(cols):
                dfs(i,j)

        return ans