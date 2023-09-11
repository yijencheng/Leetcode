class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        def b_search_row(start, end, target):
            while start<=end:
                mid = (start+end)//2
                if target<matrix[mid][0]:
                    end = mid-1
                elif target > matrix[mid][-1]:
                    start = mid+1
                else:
                    return mid
            return -1

        def b_search(start, end, target, row):
            array = matrix[row]
            
            while start<=end:
                mid = (start+end)//2

                if target<array[mid]:
                    end = mid-1
                elif target > array[mid]:
                    start = mid+1
                else:
                    return True
            return False
        
        target_row = b_search_row(0, rows-1, target)

        if target_row == -1:
            return False
        else:
            return b_search(0, cols-1, target, target_row)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0, len(matrix)-1
        while top<=bottom:
            mid = (top+bottom)//2
            if target>matrix[mid][-1]:
                top = mid+1
            elif target<matrix[mid][0]:
                bottom = mid-1
            else:
                return self.search(matrix[mid], target)
        
        return False

    def search(self, arr, target):
        left,right = 0, len(arr)-1
        
        while left<=right:
            mid = (left+right)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return False
        