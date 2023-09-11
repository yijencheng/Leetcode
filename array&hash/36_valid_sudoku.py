#tag:duplicate

#wrong
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        m = defaultdict(set)
        for i in range(rows):
            for j in range(cols):
                try:
                    cur = int(board[i][j])
                except:
                    continue

                if cur<0 or cur >9:
                    continue

                if cur in m["r"+str(i)] or cur in m["c"+str(j)] or cur in m["r"+str(i)+"c"+str(j)]:
                    return False
                m["r"+str(i)].add(cur)
                m["c"+str(j)].add(cur)
                m["r"+str(i)+"c"+str(j)].add(cur)
        return True

##success
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        m = defaultdict(set)
        for i in range(rows):
            for j in range(cols):
                try:
                    cur = int(board[i][j])
                except:
                    continue

                if cur<0 or cur >9:
                    continue

                if cur in m["r"+str(i)] or cur in m["c"+str(j)] or cur in m["r"+str(i//3)+"c"+str(j//3)]:
                    return False
                m["r"+str(i)].add(cur)
                m["c"+str(j)].add(cur)
                m["r"+str(i//3)+"c"+str(j//3)].add(cur)
        return True
                