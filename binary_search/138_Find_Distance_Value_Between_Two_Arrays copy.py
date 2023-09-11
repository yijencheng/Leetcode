#wrong
# [4,-3,-7,0,-10], [10] => min_distance=None
# root cause: return 寫錯地方
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = sorted(arr2)
        ans = 0
        
        def min_dist(num):
            start, end = 1, len(arr2)-2
            while start<=end:
                mid = (start+end)//2
                if abs(arr2[mid-1]-num) > abs(arr2[mid]-num) and abs(arr2[mid+1]-num) > abs(arr2[mid]-num):
                    return abs(arr2[mid]-num)  
                elif abs(arr2[mid-1]-num) > abs(arr2[mid]-num):
                    start = mid+1
                elif abs(arr2[mid-1]-num) < abs(arr2[mid]-num):
                    end = mid-1
                return abs(arr2[mid]-num)
            
        for num in arr1:
            if min_dist(num)>d:
                ans+=1
        return ans


# still wrong! (TLE)
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        
        def min_dist(num):
            start, end = 1, len(arr2)-2
            while start<=end:
                mid = (start+end)//2
                if abs(arr2[mid-1]-num) > abs(arr2[mid]-num) and abs(arr2[mid+1]-num) > abs(arr2[mid]-num):
                    return abs(arr2[mid]-num)  
                elif abs(arr2[mid-1]-num) > abs(arr2[mid]-num):
                    start = mid+1
                elif abs(arr2[mid-1]-num) < abs(arr2[mid]-num):
                    end = mid-1
            return abs(arr2[end]-num)
            
        for num in arr1:
            if min_dist(num)>d:
                ans+=1
        return ans

#still wrong...
[-3,10,2,8,0,10]
[-9,-1,-4,-9,-8]
9
expected: 2, actual: 3
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        
        def min_dist(num):
            start, end = 1, len(arr2)-2
            while start<=end:
                mid = (start+end)//2
                d1,d2,d3 =  abs(arr2[mid-1]-num), abs(arr2[mid]-num), abs(arr2[mid+1]-num)
                if min(d1,d2,d3) == d2:
                    return d2
                elif d1 > d2:
                    start = mid+1
                elif d1 < d2:
                    end = mid-1
            return abs(arr2[end]-num)
            
        for num in arr1:
            if min_dist(num)>d:
                ans+=1
        return ans

#TLE......
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        
        def min_dist(num):
            start, end = 1, len(arr2)-2
            while start<=end:
                mid = (start+end)//2
                d1,d2,d3 =  abs(arr2[mid-1]-num), abs(arr2[mid]-num), abs(arr2[mid+1]-num)
                if min(d1,d2,d3) == d2:
                    return d2
                elif d1 > d2:
                    start = mid+1
                elif d1 < d2:
                    end = mid-1
            return min(abs(arr2[end]-num), abs(arr2[0]-num), abs(arr2[-1]-num))
            
        for num in arr1:
            tmp = min_dist(num)
            if tmp>d:
                ans+=1
        return ans
        