
#wrong!!!
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        i,j = 0, cols-1
        
        while i<rows and j>=0 and i!=j:
            cur = matrix[i][j]
            if target > cur: i+=1
            elif target < cur: j-=1
            else: return True
        
        if matrix[i][j] == target:return True
        else:return False



# correct
# We start search the matrix from top right corner, initialize the current position to top right corner, if the target is greater than the value in current position, then the target can not be in entire row of current position because the row is sorted, if the target is less than the value in current position, then the target can not in the entire column because the column is sorted too. We can rule out one row or one column each time, so the time complexity is O(m+n).

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        i,j = 0, cols-1
        
        while i<rows and j>=0:
            cur = matrix[i][j]
            if target > cur: i+=1
            elif target < cur: j-=1
            else: return True
        
        return False