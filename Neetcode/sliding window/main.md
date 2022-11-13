#### Overview
Init pointer 

To record sliding window validity:
* larger than start >> no need (p121)
* duplicate string >> set (p3)

Medium
* charater counter >>> counter (p567)
* moving max frequency >> map + max_f (p424)

Update Left Pointer

Update Right Pointer



# Template
    l = 0
    ans = 0
    for r in range(len(XX)):
        # do sth
    return ans







#### Takeaway
# problem3: two ways of moving left ptr
sol1. while s[l] != s[r]  >>> 指針停在等號，因此要記得l+=1
sol2. while s[r] in appear >>> 指針直接停在正確的位置，但記得要再加回 appear


prolem424: 
* 更新dict時，有時候[先加] (d[key] = d.get(key,0)+1) 能夠避免不必要的keyError


prolem76
* counter 用加的比減得好
* window counter “不用”額外判別key in target_string，直接加（減）就好



* 左邊應該要縮一格(l+=1)、還是縮好幾格(while {condition} )?

Q. how to check if a dictionay's element frequency equal to a target dict?
A. use the # of count to check 
- beside dict, add a `formed`


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        found = [False]
        def dfs(i,j, wordPtr):

            if wordPtr == len(word):
                found[0] = True
                return
            if found[0] == True:return # need to add this line to early return:)

            if i<0 or i >= rows or j<0 or j>=cols or board[i][j] == "":return

            #not match
            if board[i][j] != word[wordPtr]:return
            
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
                if found[0] == True:return True # this also helps
        return found[0]
            
# TLE!!!!
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        found = [False]
        def dfs(i,j, wordPtr):

            if wordPtr == len(word):
                found[0] = True
                return

            if i<0 or i >= rows or j<0 or j>=cols or board[i][j] == "":return

            #not match
            if board[i][j] != word[wordPtr]:return
            
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
        return found[0]

            
            
            
            